from bitlist import bitlist
import hashlib

__all__ = ["hash_file", "validate_hash", "string_to_bitlist", "bitlist_to_string"]


def hash_file(file: bytes) -> str:
    """Hash bytes with SHA256 into a string"""
    rhash = hashlib.sha256(file)
    return rhash.hexdigest()


def validate_hash(org_hash: str, file: bytes) -> bool:
    """Compare the SHA256 hash of file to org_hash"""
    fhash = hashlib.sha256(file).hexdigest()
    return org_hash == fhash


def string_to_bitlist(string: str) -> bitlist:
    return bitlist(string.encode())


def bitlist_to_string(bits: bitlist) -> str:
    return bits.to_bytes().decode()
