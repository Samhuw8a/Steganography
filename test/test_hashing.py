from steganography.utils.hashing import (
    bitlist_to_string,
    string_to_bitlist,
    validate_hash,
)
from bitlist import bitlist
import pytest
from hypothesis import given
from hypothesis.strategies import text


@given(text())
def test_string_to_bitlist_reversal(text: str) -> None:
    assert bitlist_to_string(string_to_bitlist(text)) == text


@given(text(alphabet="10", min_size=1))
def test_bitlist_to_string_reversal(rbits: str) -> None:
    bits = rbits.encode("utf-8")
    assert string_to_bitlist(bitlist_to_string(bitlist(bits))) == bitlist(bits)


def test_validate_hash() -> None:
    with pytest.raises(ValueError):
        validate_hash("adsfasdf", bytes(b""))
        validate_hash("adsfasdfafadfasdfasdfasdfasddfasdf", bytes(b""))
