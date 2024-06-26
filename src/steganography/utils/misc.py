"""
Error definitions and String to bitlist conversion
"""
from __future__ import annotations

from typing import Callable, Union
from bitlist import bitlist

StringOrBytes = Union[str, bytes]
HashFunction = Callable[[bytes], str]

DEFAULT_ENCRYPTION_KEY = bytes(b"LSB-Stegagnography")


class ImageTypeError(TypeError):
    pass


class ImageModeError(TypeError):
    pass


class PayloadSizeError(ValueError):
    pass


class ExtractionError(ValueError):
    pass


class FileNameError(ExtractionError):
    pass


class FileError(ExtractionError):
    pass


# def string_to_bitlist(string: StringOrBytes) -> bitlist:
# if isinstance(string, str):
# encoded = string.encode()
# elif isinstance(string, bytes):
# encoded = string
# else:
# raise ValueError("'string' must be of type str or bytes")
# return bitlist(encoded)


# def bitlist_to_string(bits: bitlist) -> str:
# return bits.to_bytes().decode()
