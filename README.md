# FonBench

ASR benchmark and adaptation for the **Fon language** — a low-resource African tonal language (~8M speakers in Benin).

## Overview

This repository contains the code and results of a Master's thesis on automatic speech recognition for the Fon language. Six pre-trained multilingual ASR models are evaluated in zero-shot, and two adaptation strategies (LoRA and full fine-tuning) are compared on the best model.

## Results (test set, 3541 examples, 7 unseen speakers)

### Phase 1 — Zero-shot evaluation

| Model | WER | CER | Status |
|---|---|---|---|
| **MMS-1b** | 83.44% | 31.88% | Retained for Phase 2 |
| XLSR-53 | 101.03% | 64.42% | Evaluated |
| OmniASR-CTC | 92.97% | 42.46% | Evaluated |
| SeamlessM4T | 112.89% | 100.24% | Evaluated |
| Whisper-small | 165.16% | 170.10% | Evaluated |
| AfriHuBERT | 103.03% | 360.12% | Disqualified (CER>200%) |

### Phase 2 — Adaptation on MMS-1b

| Configuration | Strategy | Params trained | WER | CER |
|---|---|---|---|---|
| Zero-shot | None | 0 | 83.44% | 31.88% |
| LoRA-1 | LoRA r=8 | 2.0M (0.21%) | 32.20% | 9.08% |
| LoRA-2 | LoRA r=32 | 7.9M (0.82%) | 28.75% | 8.18% |
| FT-1 | Full FT (1e-5) | 967M (100%) | 24.32% | 7.17% |
| **FT-2** | **Full FT (5e-5)** | **967M (100%)** | **19.27%** | **6.02%** |

**Best result: WER 19.27% — a 64-point improvement over zero-shot baseline.**

## Resources

- **Interactive leaderboard**: https://huggingface.co/spaces/inesassia/fonbench-leaderboard
- **Best model (FT-2)**: https://huggingface.co/inesassia/fonbench-mms-1b-fon-ft
- **LoRA model (r=32)**: https://huggingface.co/inesassia/fonbench-mms-1b-fon-lora
- **Experiment tracking (W&B)**: https://wandb.ai/inesassiahounkponou-esgis/FonBench
- **Dataset**: https://huggingface.co/datasets/alaleye/fon

## Author

**Inès Assia HOUNKPONOU** — Master in ASR, ESGIS Bénin, 2026  
Supervisor: **Prof. Fréjus LALEYE**

## License

MIT License — see LICENSE file.
