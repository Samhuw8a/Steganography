from __future__ import annotations

from typing import List, Optional, Tuple, Iterator

from bitlist import bitlist
from numpy.typing import NDArray
from PIL.Image import Image as Img

from steganography._logging import logger
from steganography.bit_format import extract_file_and_metadata_from_raw_bits
from steganography.utils.hashing import validate_hash
from steganography.utils.misc import DEFAULT_ENCRYPTION_KEY, FileError
from steganography.utils.pixel_manipulation import encode_image_to_rgb_and_alpha_array

__all__ = ["decode_file_from_image"]


def _get_n_lsb_from_list_of_bitlists(bits: Iterator[str], n_lsb: int) -> bitlist:
    """Get the n LSB from a list of 8 bit values and returns the bits"""
    lsb: str = ""
    for i in bits:
        lsb += i[-n_lsb:]  # SCH***S ':'
    return bitlist(lsb)


def _convert_int_to_bitstring(val: int) -> str:
    """
    convert each pixel value to a bin string 0b101...
    remove prefix and pad with 0
    """
    return bin(val)[2:].zfill(8)


def _decode_bits_from_pixels(pixels: NDArray) -> Tuple[int, bitlist]:
    """Transforms pixels array and returns the lsb bits"""

    pixel_bits = (_convert_int_to_bitstring(i) for i in pixels[1:])
    # pixel_bits = [bitlist(int(i), length=8) for i in pixels]

    # Get the first 3 bits for The LSB bit's
    n_lsb_bits = _convert_int_to_bitstring(pixels[0])[-3:]
    # n_lsb_bits = pixel_bits[0][-3:].bin()

    n_lsb = int(n_lsb_bits, 2) + 1

    # get the n_lsb bits from each byte
    lsb_bits = _get_n_lsb_from_list_of_bitlists(pixel_bits, n_lsb)
    return (n_lsb, lsb_bits)


def decode_file_from_image(
    image: Img, password: Optional[str], hashing: bool = True, compression: bool = True
) -> Tuple[str, bytes]:
    """
    Decode the hidden file from an Image and validate the result if hashing is enabled.
    :param image: The Image with the hidden file
    :param password: The Password for decrypting the file (can be None)
    :param hashing: bool if hashing is encoded
    :return: Tuple[file_name, file_bytes]
    """
    # if no password is provided, then we default to DEFAULT_ENCRYPTION_KEY
    if password is None:
        encryption_key = DEFAULT_ENCRYPTION_KEY
    else:
        encryption_key = password  # type:ignore

    # get all the rgb pixels from the image
    logger.debug("loading the individual RGB values")
    rgb, _ = encode_image_to_rgb_and_alpha_array(image)
    # get the LSB bit and get all lsb-bits form the pixels
    logger.info("loading the LSB bits from the rgb values")
    n_lsb, lsb_bits = _decode_bits_from_pixels(rgb)
    logger.debug(f"got: n_lsb= {n_lsb}")
    # get all the meta data and file data from the bits
    logger.debug("extracting metadata from bits")
    file_hash, file_name, file_bytes = extract_file_and_metadata_from_raw_bits(
        lsb_bits, encryption_key, hashing, compression=True
    )
    logger.debug(f"got: file_name = {file_name}, file_hash = {file_hash}")
    if file_hash:
        # Compare the file hash for validation
        logger.debug("comparing the file against the given hash")
        if not validate_hash(file_hash, file_bytes):
            logger.debug("File hash is not equal to the given hash. Throwing FileError")
            raise FileError(
                "The File does not match the hash. The image might be corrupted."
            )
    return file_name, file_bytes
