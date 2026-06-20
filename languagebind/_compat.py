"""Compatibility shims for symbols removed from newer versions of transformers/torchaudio/torchvision."""
from __future__ import annotations

import torch
import torch.nn.functional as F

try:
    from transformers.models.clip.modeling_clip import _expand_mask
except ImportError:
    def _expand_mask(mask: torch.Tensor, dtype: torch.dtype, tgt_len: int | None = None) -> torch.Tensor:
        bsz, src_len = mask.size()
        tgt_len = tgt_len if tgt_len is not None else src_len
        expanded_mask = mask[:, None, None, :].expand(bsz, 1, tgt_len, src_len).to(dtype)
        inverted_mask = 1.0 - expanded_mask
        return inverted_mask.masked_fill(inverted_mask.to(torch.bool), torch.finfo(dtype).min)

try:
    from transformers.models.clip.modeling_clip import clip_loss
except ImportError:
    def _contrastive_loss(logits: torch.Tensor) -> torch.Tensor:
        return F.cross_entropy(logits, torch.arange(len(logits), device=logits.device))

    def clip_loss(similarity: torch.Tensor) -> torch.Tensor:
        return (_contrastive_loss(similarity) + _contrastive_loss(similarity.t())) / 2.0
