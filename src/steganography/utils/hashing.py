from bitlist import bitlist
import hashlib


def hash_file(file: bytes) -> str:
    rhash = hashlib.sha256(file)
    return rhash.hexdigest()


def validate_hash(org_hash: str, file: bytes) -> bool:
    fhash = hashlib.sha256(file).hexdigest()
    return org_hash == fhash


def string_to_bitlist(string: str) -> bitlist:
    return bitlist(string.encode())


def bitlist_to_string(bits: bitlist) -> str:
    return bits.to_bytes().decode()
