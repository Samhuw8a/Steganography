from steganography.decode import _get_n_lsb_from_list_of_bitlists
from bitlist import bitlist
from hypothesis import given
from hypothesis.strategies import lists, text


@given(lists(text(alphabet="10")))
def test_get_lsb_from_list_of_bitlists(vals: list) -> None:
    bits = list(map(bitlist, vals))
    lsb = "".join(i[-2:] for i in vals)
    assert _get_n_lsb_from_list_of_bitlists(bits, 2) == bitlist(lsb)
