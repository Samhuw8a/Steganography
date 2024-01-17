from __future__ import annotations
from typing import Callable


HashFunction = Callable[[bytes], str]


class ImageTypeError(TypeError):
    pass


class ImageModeError(TypeError):
    pass


class PayloadSizeError(ValueError):
    pass
