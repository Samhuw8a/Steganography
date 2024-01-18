from __future__ import annotations
from PIL.Image import Image as Img
from PIL import Image
from typing import IO, Tuple, Optional
from numpy.typing import NDArray
import numpy as np
from bitlist import bitlist
from steganography.utils.pixel_manipulation import encode_image_to_rgb_and_alpha_array
from steganography.bit_format import extract_file_and_metadata_from_raw_bits
from steganography.utils.misc import DEFAULT_ENCRYPTION_KEY


def _decode_file_from_pixels(pixels: NDArray) -> Tuple[Optional[str], str, bytes]:
    """Transforms pixels array and returns the result of extract_file_and_metadata_from_raw_bits"""
    # TODO ecode pixels to list[bitlist]
    # TODO determine NLSB
    # TODO construct list of all nLSB bits
    # TODO extraxt info from list of nLSB
    pixel_bits = [bitlist(int(i)) for i in pixels]
    print(pixel_bits)
    raise NotImplementedError


def decode_file_from_image(
    image: Img, password: Optional[str], hashing: bool = True
) -> IO[bytes]:
    raise NotImplementedError


_decode_file_from_pixels(np.array([255, 0]))
