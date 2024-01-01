from numpy.typing import NDArray

__all__ = ["get_max_payload_size"]

HASH = 256  # Länge des SHA-256 Hash in bits


def get_max_payload_size(pixels: NDArray, nlsb: int, lenght_bits: int = 20) -> int:
    """Max size of payload in bits"""
    vals = len(pixels) - 1  # Anzahl an Freien Pixel minus 1 für das LSB pixel
    available = vals * nlsb  # Anzahl Freier Bits nach LSB bits
    available -= lenght_bits
    available -= HASH
    return available
