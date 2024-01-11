from __future__ import annotations
import lzma
from typing import Optional
from numpy.typing import NDArray
from bitlist import bitlist
from steganography.utils.misc import HashFunction
from steganography.utils.encryption import encrypt, decrypt
from typing import Tuple, Union


__all__ = [
    "build_bits_for_file",
    "extract_file_and_metadata_from_raw_bits",
    "get_max_payload_size",
    "STEG_TAG",
]

HASH = 256  # Länge des SHA-256 Hash in bits
STEG_TAG = bytes(b"[STEG]")  # Steg Tag zum Abgränzen der versteckten Datei


def get_max_payload_size(pixels: NDArray, nlsb: int) -> int:
    """Max size of payload in bits"""
    vals = len(pixels) - 1  # Anzahl an Freien Pixel minus 1 für das LSB pixel
    available = vals * nlsb  # Anzahl Freier Bits nach LSB bits
    return available


def _add_seperator_tag_to_file(file: Union[str, bytes], tag: bytes) -> bytes:
    """Returns file bytes with added Tag; 'tag file tag'"""
    if isinstance(file, bytes):
        bfile = file
    else:
        bfile = file.encode()
    return tag + bfile + tag


def _seperate_filename_and_content(
    bits: bitlist, tag: bytes = STEG_TAG
) -> Tuple[bytes, bytes]:
    """Seperate filename and file_content by spliting on tag"""
    filename, _, content = bits.to_bytes().partition(tag)
    content = content.split(tag)[0]
    return filename, content


def _compress_file(file: bytes) -> bytes:
    return lzma.compress(file)


def _decompress_file(file: Union[str, bytes]) -> bytes:
    if isinstance(file, str):
        file = file.encode()
    return lzma.decompress(file)


def build_bits_for_file(
    file_content: bytes,
    file_name: str,
    hash_func: Optional[HashFunction],
    encryption_key: bytes,
    steg_tag: bytes = STEG_TAG,
) -> bitlist:
    """
    Build to corect bits for embeding into the pixels. The NLSB pixel has to be encoded seperate.
    :param file_content: encoded and compressed file bytes
    :param file_name: the filename
    :param hash_func: function for hashing the file bytes
    :param encryption_key: the passkey for the AES Cypher
    :opt-param steg_tag the Tag used to seperate the file content
    :return: bits for embeding
    """
    if hash_func:
        file_hash = bitlist.fromhex(hash_func(file_content))
    compressed = _compress_file(file_content)
    ecrypted = encrypt(encryption_key, compressed, False)
    with_tag = _add_seperator_tag_to_file(ecrypted, STEG_TAG)
    file = bitlist(with_tag)
    filename_bits = bitlist(bytes(file_name.encode()))
    bits = file_hash.bin() if hash_func else "" + filename_bits.bin() + file.bin()
    return bitlist(bits)


def extract_file_and_metadata_from_raw_bits(
    extracted_bits: bitlist,
    encryption_key: bytes,
    hashing: bool = True,
    steg_tag: bytes = STEG_TAG,
) -> Tuple[Optional[str], str, bytes]:
    """
    Get the file and corresponding metadata from to full set of bits. Not including NLSB bit.
    :param extracted_bits: all of the n_LSB bits from the file
    :param encryption_key: the passkey for the AES Cypher
    :param hashing: bool if hashing is encoded
    :opt-param steg_tag the Tag used to seperate the file content
    :return: Tuple[file_hash, file_name, file_bytes]
    """
    if hashing:
        file_hash = extracted_bits[:256]
        extracted_bits = extracted_bits[256:]
    file_name, file_content = _seperate_filename_and_content(
        extracted_bits, tag=STEG_TAG
    )
    decrypted = decrypt(encryption_key, file_content, False)
    decompressed = _decompress_file(decrypted)

    return (file_hash.hex() if hashing else None, file_name.decode(), decompressed)
