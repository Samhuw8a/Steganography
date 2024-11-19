import random
from more_itertools import chunked
from hypothesis import given
from hypothesis.strategies import text
from steganography.decode import _get_n_lsb_from_list_of_bits, _convert_int_to_bitstring


@given(text(alphabet="10", min_size=1))
def test_get_n_lsb_from_list_of_bits1(bits: str):
    data = ("".join(random.choices("10", k=7)) + i for i in bits)
    assert _get_n_lsb_from_list_of_bits(data, 1) == bits


@given(text(alphabet="10", min_size=2))
def test_get_n_lsb_from_list_of_bits2(bits: str):
    bits = bits + "0" * (2 - len(bits) % 2)
    data = ("".join(random.choices("10", k=6)) + "".join(i) for i in chunked(bits, 2))
    assert _get_n_lsb_from_list_of_bits(data, 2) == bits


@given(text(alphabet="10", min_size=3))
def test_get_n_lsb_from_list_of_bits3(bits: str):
    bits = bits + "0" * (3 - len(bits) % 3)
    data = ("".join(random.choices("10", k=5)) + "".join(i) for i in chunked(bits, 3))
    assert _get_n_lsb_from_list_of_bits(data, 3) == bits


@given(text(alphabet="10", min_size=4))
def test_get_n_lsb_from_list_of_bits4(bits: str):
    bits = bits + "0" * (4 - len(bits) % 4)
    data = ("".join(random.choices("10", k=4)) + "".join(i) for i in chunked(bits, 4))
    assert _get_n_lsb_from_list_of_bits(data, 4) == bits


@given(text(alphabet="10", min_size=5))
def test_get_n_lsb_from_list_of_bits5(bits: str):
    bits = bits + "0" * (5 - len(bits) % 5)
    data = ("".join(random.choices("10", k=3)) + "".join(i) for i in chunked(bits, 5))
    assert _get_n_lsb_from_list_of_bits(data, 5) == bits


@given(text(alphabet="10", min_size=6))
def test_get_n_lsb_from_list_of_bits6(bits: str):
    bits = bits + "0" * (6 - len(bits) % 6)
    data = ("".join(random.choices("10", k=4)) + "".join(i) for i in chunked(bits, 6))
    assert _get_n_lsb_from_list_of_bits(data, 6) == bits


@given(text(alphabet="10", min_size=7))
def test_get_n_lsb_from_list_of_bits7(bits: str):
    bits = bits + "0" * (7 - len(bits) % 7)
    data = ("".join(random.choices("10", k=1)) + "".join(i) for i in chunked(bits, 7))
    assert _get_n_lsb_from_list_of_bits(data, 7) == bits


@given(text(alphabet="10", min_size=8))
def test_get_n_lsb_from_list_of_bits8(bits: str):
    data = (i for i in bits)
    assert _get_n_lsb_from_list_of_bits(data, 8) == bits


@given(text(alphabet="10", min_size=8, max_size=8))
def test_convert_int_to_bitstring(x: str):
    assert _convert_int_to_bitstring(int(x, 2)) == x
