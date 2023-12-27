import pytest
from steganography.utils.bit_manipulation import set_bit, set_n_LSB


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


def test_set_n_LSB() -> None:
    assert set_n_LSB(255, 1, (0,)) == 254
    assert set_n_LSB(255, 1, [0]) == 254

    assert set_n_LSB(255, 2, (0, 0)) == 252
    assert set_n_LSB(255, 3, (0, 1, 0)) == 250
    with pytest.raises(ValueError):
        set_n_LSB(255, 4, (0,))
        set_n_LSB(255, 4, (0, 1))
        set_n_LSB(255, 4, (0, 1, 1))
        set_n_LSB(255, 4, (0, 1, 0, 1, 0))
