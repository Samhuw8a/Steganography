from numpy.typing import NDArray
from bitlist import bitlist
from steganography.utils.misc import HashFunction


__all__ = ["get_max_payload_size"]

HASH = 256  # Länge des SHA-256 Hash in bits


def get_max_payload_size(pixels: NDArray, nlsb: int, lenght_bits: int = 20) -> int:
    """Max size of payload in bits"""
    vals = len(pixels) - 1  # Anzahl an Freien Pixel minus 1 für das LSB pixel
    available = vals * nlsb  # Anzahl Freier Bits nach LSB bits
    available -= lenght_bits
    available -= HASH
    if available <= 0:
        raise ValueError("The pixels array is to small to store any data")
    return available


def build_bits_for_file(file_content: bytes, hash_func: HashFunction) -> bitlist:
    # TODO hash file
    # TODO convert hash to bitlist
    return NotImplemented
