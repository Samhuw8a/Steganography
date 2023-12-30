from steganography.utils.hashing import (
    bitlist_to_string,
    string_to_bitlist,
    validate_hash,
)
from bitlist import bitlist
import pytest


def test_string_to_bitlist_reversal() -> None:
    assert bitlist_to_string(string_to_bitlist("asdfghjkl")) == "asdfghjkl"
    assert bitlist_to_string(string_to_bitlist("123456789")) == "123456789"
    assert bitlist_to_string(string_to_bitlist(".,#<>()[]{}")) == ".,#<>()[]{}"
    assert bitlist_to_string(string_to_bitlist("\n\t")) == "\n\t"


def test_bitlist_to_string_reversal() -> None:
    b1 = bitlist("1101010101")
    b2 = bitlist("000010100101001010")
    b3 = bitlist("1010101010101")
    b4 = bitlist("1")
    assert string_to_bitlist(bitlist_to_string(b1)) == b1
    assert string_to_bitlist(bitlist_to_string(b2)) == b2
    assert string_to_bitlist(bitlist_to_string(b3)) == b3
    assert string_to_bitlist(bitlist_to_string(b4)) == b4


def test_validate_hash() -> None:
    with pytest.raises(ValueError):
        validate_hash("adsfasdf", bytes(b""))
        validate_hash("adsfasdfafadfasdfasdfasdfasddfasdf", bytes(b""))
