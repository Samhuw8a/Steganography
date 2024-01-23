from __future__ import annotations

import hashlib
from typing import Union

from bitlist import bitlist

StringOrBytes = Union[str, bytes]
__all__ = ["hash_file", "validate_hash", "string_to_bitlist", "bitlist_to_string"]


def hash_file(file: bytes) -> str:
    """Hash bytes with SHA256 into a string"""
    rhash = hashlib.sha256(file)
    return rhash.hexdigest()


def validate_hash(org_hash: str, file: bytes) -> bool:
    """Compare the SHA256 hash of file to org_hash"""
    if not len(org_hash) == 64:
        raise ValueError("org_hash has to be a valid SHA256 hash")
    fhash = hashlib.sha256(file).hexdigest()
    return org_hash == fhash


def string_to_bitlist(string: StringOrBytes) -> bitlist:
    if isinstance(string, str):
        encoded = string.encode()
    elif isinstance(string, bytes):
        encoded = string
    else:
        raise ValueError("'string' must be of type str or bytes")
    return bitlist(encoded)


def bitlist_to_string(bits: bitlist) -> str:
    return bits.to_bytes().decode()
