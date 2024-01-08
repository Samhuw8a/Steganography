from __future__ import annotations
import lzma
from typing import IO, Tuple

import numpy as np
from numpy.typing import NDArray
from PIL.Image import Image as Img

from steganography.utils.misc import ImageModeException, ImageTypeException
from steganography.utils.pixel_manipulation import seperate_rgb_and_alpha

__all__ = ["encode_file_in_image"]


def _encode_image_to_rgb_and_alpha_array(image: Img) -> Tuple[NDArray, NDArray]:
    """Convert the Image to a usable mode and split into rgb and alpha array"""
    if image.format != "PNG":
        raise ImageTypeException(
            "The Provided Image has to be of Type: 'PNG' got '{image.format}'"
        )
    imgtype = image.mode
    if imgtype == "P":
        image = image.convert("RGBA")
    elif imgtype == "RGB":
        rgb = np.array(image).flatten()
        alpha = np.zeros(len(rgb) // 3, dtype=int)
        return (rgb, alpha)
    elif imgtype != "RGBA":
        raise ImageModeException(f"Can't handle Imagemode: {imgtype}")

    assert image.mode == "RGBA"
    pixels = np.array(image).flatten()
    rgb, alpha = seperate_rgb_and_alpha(pixels)
    return (rgb, alpha)


def _compress_file(file: bytes) -> bytes:
    return lzma.compress(file)


def encode_file_in_image(file: IO[bytes], image: Img, n_lsb: int) -> Img:
    return NotImplemented
