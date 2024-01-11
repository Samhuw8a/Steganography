from __future__ import annotations
from typing import IO, Tuple

import numpy as np
from numpy.typing import NDArray
from PIL.Image import Image as Img

from steganography.utils.misc import ImageModeException, ImageTypeException
from steganography.utils.pixel_manipulation import (
    seperate_rgb_and_alpha,
    embed_bits_in_pixels,
)
from steganography.utils.hashing import hash_file
from steganography.bit_format import STEG_TAG, build_bits_for_file, get_max_payload_size

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


def _encode_file_in_pixels(
    pixels: NDArray,
    file_content: bytes,
    file_name: str,
    encryption_key: bytes,
    n_lsb: int,
) -> NDArray:
    """encode the file and Metadata into a flattened rgb-array"""
    max_size = get_max_payload_size(pixels, n_lsb, tag=STEG_TAG)
    file_size = len(file_content) * 8 + len(file_name.encode()) * 8
    if file_size > max_size:
        raise ValueError("the File and filename are too big to store into the Image")
    bits = build_bits_for_file(
        file_content, file_name, hash_file, encryption_key, steg_tag=STEG_TAG
    )
    embeded_pixels = embed_bits_in_pixels(pixels, bits, n_lsb)
    return embeded_pixels


def encode_file_in_image(file: IO[bytes], image: Img, n_lsb: int) -> Img:
    return NotImplemented
