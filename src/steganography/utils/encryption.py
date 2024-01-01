import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from typing import Union


def encrypt(key: str, source: bytes) -> bytes:
    return NotImplemented


def decrypt(key: str, source: bytes) -> bytes:
    return NotImplemented
