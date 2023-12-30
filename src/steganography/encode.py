from PIL import Image
from PIL.Image import Image as Img
import numpy as np
from numpy.typing import NDArray
from bitlist import bitlist
from typing import IO, Tuple
from steganography.utils.misc import (
    HashFunction,
    ImageTypeException,
    ImageModeException,
)
from steganography.utils.pixel_manipulation import seperate_rgb_and_alpha


__all__ = ["encode_file_in_image"]


def _encode_image_to_rgb_and_alpha_array(image: Img) -> Tuple[NDArray, NDArray]:
    "Split image into rgb and alpha array"
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


def _build_bits_for_file(file_content: bytes, hash_func: HashFunction) -> bitlist:
    # TODO hash file
    # TODO convert hash to bitlist
    return NotImplemented


def encode_file_in_image(file: IO[bytes], image: Img, n_lsb: int) -> Img:
    return NotImplemented
