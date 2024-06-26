import pytest
from hypothesis import given
from hypothesis.strategies import binary

from steganography.utils.hashing import (
    hash_file,
    validate_hash,
)


def test_validate_hash_raises() -> None:
    with pytest.raises(ValueError):
        validate_hash("adsfasdf", bytes(b""))
        validate_hash("adsfasdfafadfasdfasdfasdfasddfasdf", bytes(b""))


@given(binary())
def test_validate_hash(cont: bytes) -> None:
    h = hash_file(cont)
    assert validate_hash(h, cont)
