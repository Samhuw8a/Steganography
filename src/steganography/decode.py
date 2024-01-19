from __future__ import annotations
from PIL.Image import Image as Img
from PIL import Image
from typing import IO, Tuple, Optional, List
from numpy.typing import NDArray
import numpy as np
from bitlist import bitlist
from steganography.utils.pixel_manipulation import encode_image_to_rgb_and_alpha_array
from steganography.bit_format import extract_file_and_metadata_from_raw_bits
from steganography.utils.misc import DEFAULT_ENCRYPTION_KEY


def _get_n_lsb_from_list_of_bitlists(bits: List[bitlist], n_lsb: int) -> bitlist:
    """Get the n LSB from a list of 8 bit values and returns the bits"""
    lsb: str = ""
    for i in bits:
        lsb += i.bin()[-n_lsb:]
    return bitlist(lsb)


def _decode_bits_from_pixels(pixels: NDArray) -> Tuple[int, bitlist]:
    """Transforms pixels array and returns the lsb bits"""
    pixel_bits = [bitlist(int(i), length=8) for i in pixels]
    n_lsb_bits = pixel_bits[0][-3:].bin()
    n_lsb = int(n_lsb_bits, 2) + 1
    lsb_bits = _get_n_lsb_from_list_of_bitlists(pixel_bits[1:], n_lsb)

    return (n_lsb, lsb_bits)


def decode_file_from_image(
    image: Img, password: Optional[str], hashing: bool = True
) -> IO[bytes]:
    # TODO read Image_pixels
    # TODO transform pixels
    # TODO extract_file
    # TODO decompress
    # TODO dectypt
    # TODO compare Hash
    # TODO Raise high-level Errors
    # TODO Parameter checking
    raise NotImplementedError
