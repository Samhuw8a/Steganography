import pytest
from bitlist import bitlist
from hypothesis import given
from hypothesis.strategies import binary, text

from steganography.utils.hashing import (
    bitlist_to_string,
    hash_file,
    string_to_bitlist,
    validate_hash,
)


@given(text())
def test_string_to_bitlist_reversal(text: str) -> None:
    assert bitlist_to_string(string_to_bitlist(text)) == text


@given(text(alphabet="10", min_size=1))
def test_bitlist_to_string_reversal(rbits: str) -> None:
    bits = rbits.encode("utf-8")
    assert string_to_bitlist(bitlist_to_string(bitlist(bits))) == bitlist(bits)


def test_validate_hash_raises() -> None:
    with pytest.raises(ValueError):
        validate_hash("adsfasdf", bytes(b""))
        validate_hash("adsfasdfafadfasdfasdfasdfasddfasdf", bytes(b""))


@given(binary())
def test_validate_hash(cont: bytes) -> None:
    h = hash_file(cont)
    assert validate_hash(h, cont)
