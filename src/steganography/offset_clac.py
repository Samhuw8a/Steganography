from numpy.typing import NDArray

__all__ = ["get_max_payload_size"]

LENGHT = 20  # Lenge der Payload in Bits
HASH = 256  # Länge des SHA-256 Hash in bits


def get_max_payload_size(pixels: NDArray, nlsb: int) -> int:
    """Max size of payload in bits"""
    vals = len(pixels) - 1  # Anzahl an Freien Pixel minus 1 für das LSB pixel
    available = vals * nlsb  # Anzahl Freier Bits nach LSB bits
    available -= LENGHT
    available -= HASH
    return available
