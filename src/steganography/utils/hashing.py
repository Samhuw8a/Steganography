from typing import Any
import hashlib


def hash_file(file: bytes) -> str:
    rhash = hashlib.sha256(file)
    return rhash.hexdigest()


def validate_hash(org_hash: str, file: bytes) -> bool:
    fhash = hashlib.sha256(file).hexdigest()
    return org_hash == fhash
