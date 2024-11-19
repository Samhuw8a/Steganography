"""
Error definitions
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
