# Future Project Decision Memo

## Purpose

This memo records future project options after the small-scale SimCLR reproduction and ablation project is complete.

## Current Decision

- Status: not decided
- Decision owner: Human Owner
- Current focus: finish the SimCLR research-engineering baseline before starting audio or audio-visual implementation work.

## Candidate Directions

| Direction | Description | Relationship to This Project | Implement Now? |
|---|---|---|---|
| Audio-SimCLR | Apply contrastive learning ideas to audio representations. | Natural follow-up after understanding SimCLR augmentations, embeddings, and linear probing. | No |
| CLAP-lite | Study audio-text contrastive learning at a small scale. | Extends contrastive learning from image-image pairs to cross-modal pairs. | No |
| Audio-Visual Synchronization | Learn representations from aligned or misaligned audio-video pairs. | Moves from unimodal contrastive learning to audio-visual intelligence. | No |

## Decision Criteria

- The current SimCLR implementation is complete and understandable.
- Gate 0 through Gate 5 evidence is documented.
- Baseline and ablation results are real, traceable, and reviewed.
- Required compute, datasets, and storage paths are clear.
- The Human Owner can explain the method, losses, tensor shapes, and limitations.

## Not in Current Scope

- Audio training implementation.
- Video data processing.
- Large audio-visual datasets.
- AV-HuBERT or ImageBind reproduction.
- Claims that CIFAR-10 SimCLR results prove audio-visual performance.

## Next Review Point

Revisit this memo after the final SimCLR report is drafted and the owner has reviewed the baseline, ablation, and limitation sections.
