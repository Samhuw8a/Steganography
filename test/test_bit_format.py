from steganography.bit_format import _compress_file, _decompress_file
from hypothesis.strategies import binary
from hypothesis import given


@given(binary())
def test_compress_decompress_reversal(cont: bytes) -> None:
    assert _decompress_file(_compress_file(cont)) == cont
