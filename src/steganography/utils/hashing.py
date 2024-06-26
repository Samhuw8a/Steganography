"""
A Collection of functions for hashing files and comparing hashes against files
"""
from __future__ import annotations

import hashlib
from typing import Union


StringOrBytes = Union[str, bytes]
__all__ = ["hash_file", "validate_hash"]


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
