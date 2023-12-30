from steganography.utils.hashing import bitlist_to_string, string_to_bitlist


def test_string_to_bitlist_reversal() -> None:
    assert bitlist_to_string(string_to_bitlist("asdfghjkl")) == "asdfghjkl"
    assert bitlist_to_string(string_to_bitlist("123456789")) == "123456789"
    assert bitlist_to_string(string_to_bitlist(".,#<>()[]{}")) == ".,#<>()[]{}"
    assert bitlist_to_string(string_to_bitlist("\n\t")) == "\n\t"
