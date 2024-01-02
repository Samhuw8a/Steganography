from numpy.typing import NDArray
from bitlist import bitlist
from steganography.utils.misc import HashFunction
from typing import Tuple


__all__ = ["build_bits_for_file", "extract_file_and_metadata_from_raw_bits"]

HASH = 256  # Länge des SHA-256 Hash in bits


def _get_max_payload_size(pixels: NDArray, nlsb: int, lenght_bits: int = 20) -> int:
    """Max size of payload in bits"""
    vals = len(pixels) - 1  # Anzahl an Freien Pixel minus 1 für das LSB pixel
    available = vals * nlsb  # Anzahl Freier Bits nach LSB bits
    available -= lenght_bits
    available -= HASH
    if available <= 0:
        raise ValueError("The pixels array is to small to store any data")
    return available


def build_bits_for_file(
    file_content: bytes, file_name: str, hash_func: HashFunction
) -> bitlist:
    """
    Build to corect bits for embeding into the pixels. The NLSB pixel has to be encoded seperate.
    :param file_content: encoded and compressed file bytes
    :param file_name: the filename
    :param hash_func: function for hashing the file bytes
    :return: bits for embeding
    """
    return NotImplemented


def extract_file_and_metadata_from_raw_bits(
    extracted_bits: bitlist,
) -> Tuple[str, str, bytes]:
    """
    Get the file and corresponding metadata from to full set of bits. Not including NLSB bit.
    :param extracted_bits: all of the n_LSB bits from the file
    :return: Tuple[file_hash, file_name, file_bytes]
    """
    return NotImplemented
