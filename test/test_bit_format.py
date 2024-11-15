from steganography.bit_format import (
    _compress_file,
    _decompress_file,
    build_bits_for_file,
    extract_file_and_metadata_from_raw_bits,
)
from steganography.utils.hashing import hash_file
from hypothesis.strategies import binary, text
from hypothesis import given


@given(binary())
def test_compress_decompress_reversal(cont: bytes) -> None:
    assert _decompress_file(_compress_file(cont)) == cont


@given(file=binary(), name=text(), key=binary())
def test_build_extract_reversal(file: bytes, name: str, key: bytes) -> None:
    bits = build_bits_for_file(file, name, hash_file, key)
    strbits = "".join(str(i) for i in bits)
    assert (hash_file(file), name, file) == extract_file_and_metadata_from_raw_bits(
        strbits, key
    )


@given(file=binary(), name=text(), key=binary())
def test_build_extract_reversal_no_hash(file: bytes, name: str, key: bytes) -> None:
    bits = build_bits_for_file(file, name, None, key)
    strbits = "".join(str(i) for i in bits)
    assert (None, name, file) == extract_file_and_metadata_from_raw_bits(
        strbits, key, hashing=False
    )
