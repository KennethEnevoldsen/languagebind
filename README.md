# languagebind

[LanguageBind](https://github.com/PKU-YuanGroup/LanguageBind) (ICLR 2024) packaged as a pip-installable library with compatibility patches for modern `transformers`, `torchvision`, and `torchaudio`.

The original LanguageBind repo has no `pyproject.toml`, so it cannot be installed via pip. This package provides that, plus inline patches for five breaking changes introduced in newer dependency versions.

## Installation

```bash
pip install languagebind
```

For video support:
```bash
pip install "languagebind[video]"
```

For audio support:
```bash
pip install "languagebind[audio]"
```

## Usage

```python
from languagebind import (
    LanguageBindVideo, LanguageBindVideoProcessor, LanguageBindVideoTokenizer,
    LanguageBindAudio, LanguageBindAudioProcessor, LanguageBindAudioTokenizer,
    LanguageBindImage, LanguageBindImageProcessor, LanguageBindImageTokenizer,
)
```

## Compatibility patches

- `_expand_mask` / `clip_loss`: removed from `transformers` 4.40+, re-implemented in `languagebind._compat`
- `torchaudio.set_audio_backend()`: deprecated, guarded with `try/except`
- `torchvision.transforms._transforms_video`: private API fallback to public `torchvision.transforms` equivalents
- `CLIPTokenizer.__init__` positional args: changed to keyword args for `transformers` 4.40+ compatibility

## License

MIT — same as the original [LanguageBind](https://github.com/PKU-YuanGroup/LanguageBind).
