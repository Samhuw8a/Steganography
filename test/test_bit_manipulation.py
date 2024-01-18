import pytest
from bitlist import bitlist

from steganography.utils.bit_manipulation import set_bit, set_LSB, set_lsb_bit
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=0, max_value=255), integers(min_value=1, max_value=8))
def test_set_lsb_bit(val: int, lsb: int) -> None:
    bits = list(bitlist(lsb - 1, length=3))
    assert set_lsb_bit(val, lsb) == set_LSB(val, 3, bits)


def test_set_bit() -> None:
    assert set_bit(255, 0, 0) == 254
    assert set_bit(255, 1, 0) == 253
    assert set_bit(171, 0, 0) == 170
    assert set_bit(171, 5, 0) == 139
    assert set_bit(10, 3, 0) == 2
    assert set_bit(2, 0, 1) == 3
    assert set_bit(0, 0, 1) == 1

    assert set_bit(255, 0, False) == 254
    assert set_bit(255, 1, False) == 253
    assert set_bit(171, 0, False) == 170
    assert set_bit(171, 5, False) == 139
    assert set_bit(10, 3, False) == 2
    assert set_bit(2, 0, True) == 3
    assert set_bit(0, 0, True) == 1

    with pytest.raises(ValueError):
        set_bit(255, 0, 3)
        set_bit(255, 0, 3)
        set_bit(255, 0, -1000)
        set_bit(255, 0, -1)


def test_set_LSB() -> None:
    assert set_LSB(255, 1, (0,)) == 254
    assert set_LSB(255, 1, [0]) == 254

    assert set_LSB(255, 2, (0, 0)) == 252
    assert set_LSB(255, 3, (0, 1, 0)) == 250
    with pytest.raises(ValueError):
        # n!=len(x)
        set_LSB(255, 4, (0,))
        set_LSB(255, 4, (0, 1))
        set_LSB(255, 4, (0, 1, 1))
        set_LSB(255, 4, (0, 1, 0, 1, 0))
        # n not between 1 and 8
        set_LSB(255, 0, tuple())
        set_LSB(255, 9, (1, 1, 1, 1, 1, 1, 1, 1, 1))
