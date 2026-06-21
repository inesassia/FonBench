import numpy as np
from jiwer import wer, cer
import sys

def make_compute_metrics(processor, twer_module_path):
    if twer_module_path not in sys.path:
        sys.path.insert(0, twer_module_path)
    from twer import calculer_twer
    def compute_metrics(pred):
        pred_ids = np.argmax(pred.predictions, axis=-1)
        pred.label_ids[pred.label_ids == -100] = processor.tokenizer.pad_token_id
        pred_str  = processor.batch_decode(pred_ids)
        label_str = processor.batch_decode(pred.label_ids, group_tokens=False)
        pairs = [(p, l) for p, l in zip(pred_str, label_str) if l.strip()]
        if not pairs:
            return {"wer": 1.0, "cer": 1.0, "twer": 1.0, "wer_tonal": 0.0, "wer_segmental": 1.0}
        preds, labels = zip(*pairs)
        preds, labels = list(preds), list(labels)
        twer_res = calculer_twer(labels, preds, alpha=2.0)
        return {"wer": wer(labels, preds), "cer": cer(labels, preds),
                "twer": twer_res["twer"], "wer_tonal": twer_res["wer_tonal"],
                "wer_segmental": twer_res["wer_segmental"]}
    return compute_metrics
