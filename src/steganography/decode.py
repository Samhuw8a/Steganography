from __future__ import annotations
from PIL.Image import Image as Img
from typing import Tuple, Optional, List
from numpy.typing import NDArray
from bitlist import bitlist
from steganography.utils.pixel_manipulation import encode_image_to_rgb_and_alpha_array
from steganography.bit_format import extract_file_and_metadata_from_raw_bits
from steganography.utils.misc import DEFAULT_ENCRYPTION_KEY
from steganography.utils.hashing import validate_hash

__all__ = ["decode_file_from_image"]


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
) -> Tuple[str, bytes]:
    """
    Decode the hidden file from an Image and validate the result if hashing is enabled.
    :param image: The Image with the hidden file
    :param password: The Password for decrypting the file (can be None)
    :param hashing: bool if hashing is encoded
    :return: Tuple[file_name, file_bytes]
    """
    if password is None:
        encryption_key = DEFAULT_ENCRYPTION_KEY
    else:
        encryption_key = password  # type:ignore
    rgb, alpha = encode_image_to_rgb_and_alpha_array(image)
    n_lsb, lsb_bits = _decode_bits_from_pixels(rgb)
    print(lsb_bits.to_bytes()[:300])
    file_hash, file_name, file_bytes = extract_file_and_metadata_from_raw_bits(
        lsb_bits, encryption_key, hashing
    )
    if file_hash:
        if validate_hash(file_hash, file_bytes):
            # TODO Raise high Level Error
            raise NotImplementedError
    # TODO Parameter checking
    return file_name, file_bytes
