import unicodedata
from jiwer import wer

DIACRITIQUES_TONALS = {
    chr(0x0300), chr(0x0301), chr(0x0302), chr(0x0303), chr(0x0304),
    chr(0x0306), chr(0x0307), chr(0x0308), chr(0x030c),
    chr(0x00e0), chr(0x00e1), chr(0x00e8), chr(0x00e9),
    chr(0x00ec), chr(0x00ed), chr(0x00f2), chr(0x00f3),
    chr(0x00f9), chr(0x00fa), chr(0x0115), chr(0x012d),
    chr(0x014f), chr(0x016d),
}

def contient_ton(mot):
    for c in mot:
        if c in DIACRITIQUES_TONALS:
            return True
        for d in unicodedata.normalize("NFD", c):
            if d in DIACRITIQUES_TONALS:
                return True
    return False

def strip_tons(mot):
    result = ""
    for c in mot:
        decomposed = unicodedata.normalize("NFD", c)
        base = "".join(d for d in decomposed if d not in DIACRITIQUES_TONALS)
        result += unicodedata.normalize("NFC", base)
    return result

def calculer_twer(references, hypotheses, alpha=2.0):
    refs_seg, hyps_seg, refs_ton, hyps_ton = [], [], [], []
    for ref, hyp in zip(references, hypotheses):
        rw = ref.strip().split(); hw = hyp.strip().split()
        refs_seg.append(" ".join(strip_tons(w) for w in rw))
        hyps_seg.append(" ".join(strip_tons(w) for w in hw))
        refs_ton.append(" ".join(w for w in rw if contient_ton(w)))
        hyps_ton.append(" ".join(w for w in hw if contient_ton(w)))
    wer_seg = wer(refs_seg, hyps_seg) if any(r.strip() for r in refs_seg) else 0.0
    valid = [(r, h) for r, h in zip(refs_ton, hyps_ton) if r.strip()]
    wer_ton = wer([r for r,h in valid], [h for r,h in valid]) if valid else 0.0
    return {"twer": wer_seg + alpha*wer_ton, "wer_segmental": wer_seg, "wer_tonal": wer_ton}
