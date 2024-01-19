from __future__ import annotations
from typing import IO, Optional

from numpy.typing import NDArray
import numpy as np
from PIL.Image import Image as Img
from PIL import Image

from steganography.utils.misc import (
    PayloadSizeError,
    HashFunction,
    DEFAULT_ENCRYPTION_KEY,
)
from steganography.utils.bit_manipulation import set_lsb_bit
from steganography.utils.pixel_manipulation import (
    encode_image_to_rgb_and_alpha_array,
    embed_bits_in_pixels,
    combine_rgb_and_alpha,
    build_pixel_array,
)
from steganography.utils.hashing import hash_file
from steganography.bit_format import STEG_TAG, build_bits_for_file, get_max_payload_size

__all__ = ["encode_file_in_image"]

DEFAULT_ENCRYPTION_KEY = bytes(b"LSB-Stegagnography")


def _encode_file_in_pixels(
    pixels: NDArray,
    file_content: bytes,
    file_name: str,
    encryption_key: bytes,
    n_lsb: int,
    hash_func: Optional[HashFunction],
) -> NDArray:
    """encode the file and Metadata into a flattened rgb-array"""
    max_size = get_max_payload_size(pixels, n_lsb)
    bits = build_bits_for_file(
        file_content, file_name, hash_func, encryption_key, steg_tag=STEG_TAG
    )
    if len(bits) > max_size:
        raise PayloadSizeError(
            "the File and filename are too big to store into the Image"
        )
    embeded_pixels = embed_bits_in_pixels(pixels, bits, n_lsb)
    return embeded_pixels


def encode_file_in_image(
    file_bytes: bytes,
    file_name: str,
    image: Img,
    n_lsb: int,
    encryption_key: Optional[str] = None,
    hashing: bool = True,
) -> Img:
    """
    Encode file into image
    :param file: the file you intend to hide
    :param file_name: the filename
    :param image: Coverimage which is modified
    :param n_lsb: the number of least significant bits which are modified
    :param encryption_key: the key used for encryption. If it is not specified, a default key is used.
    :return: Modified Image
    """
    if encryption_key is None:
        AES_key = DEFAULT_ENCRYPTION_KEY
    else:
        AES_key = bytes(encryption_key.encode())
    hash_func: Optional[HashFunction] = hash_file if hashing else None
    width, height = image.size
    argb, alphas = encode_image_to_rgb_and_alpha_array(image)
    rgb = argb[1:]
    lsb_val = argb[0]
    new_lsb_val = set_lsb_bit(lsb_val, n_lsb)
    embeded_rgb = _encode_file_in_pixels(
        rgb, file_bytes, file_name, AES_key, n_lsb, hash_func
    )
    new_rgb: NDArray = np.insert(embeded_rgb, 0, new_lsb_val)
    from steganography.decode import _get_n_lsb_from_list_of_bitlists
    from bitlist import bitlist

    print(
        _get_n_lsb_from_list_of_bitlists(
            [bitlist(int(i)) for i in new_rgb], n_lsb
        ).to_bytes()[:300]
    )
    new_flatt_image_array = combine_rgb_and_alpha(new_rgb, alphas)
    new_image_array = build_pixel_array(new_flatt_image_array, width, height)
    return Image.fromarray(new_image_array)
