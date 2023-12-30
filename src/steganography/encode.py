from PIL import Image
from PIL.Image import Image as Img
import numpy as np
from numpy.typing import NDArray
from bitlist import bitlist
from typing import IO, Tuple
from steganography.utils.misc import *

#  from steganography.utils.misc import test

__all__ = ["encode_file_in_image"]


def _encode_image_to_flatt_and_alpha_array(image: Img) -> Tuple[NDArray]:
    # TODO check Image type
    # TODO convert Image type
    # TODO return pixel and alpha list
    return NotImplemented


def _build_bits_for_file(file_content: bytes, hash_func: HashFunction) -> bitlist:
    # TODO hash file
    # TODO convert hash to bitlist
    return NotImplemented


def encode_file_in_image(file: IO[bytes], image: Img, n_lsb: int) -> Img:
    return NotImplemented
