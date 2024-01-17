from __future__ import annotations
from PIL.Image import Image as Img
from numpy.typing import NDArray


def _decode_file_from_pixels() -> NDArray:
    raise NotImplementedError


def decode_file_from_image() -> Img:
    raise NotImplementedError
