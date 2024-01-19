from steganography.decode import _get_n_lsb_from_list_of_bitlists
from bitlist import bitlist
from hypothesis import given
from hypothesis.strategies import lists, text, integers


@given(lists(text(alphabet="10")), integers(min_value=0, max_value=8))
def test_get_lsb_from_list_of_bitlists(vals: list, n: int) -> None:
    bits = list(map(bitlist, vals))
    lsb = "".join(i[-n:] for i in vals)
    assert _get_n_lsb_from_list_of_bitlists(bits, n) == bitlist(lsb)
