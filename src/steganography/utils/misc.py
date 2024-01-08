from __future__ import annotations
from typing import Callable


HashFunction = Callable[[bytes], str]


class ImageTypeException(TypeError):
    pass


class ImageModeException(TypeError):
    pass
