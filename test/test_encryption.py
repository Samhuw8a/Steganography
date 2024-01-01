from steganography.utils.encryption import encrypt, decrypt
from hypothesis import given
from hypothesis.strategies import binary


@given(data=binary(), key=binary())
def test_encrypt_decrypt_reversal(data: bytes, key: bytes) -> None:
    assert data == decrypt(key, (encrypt(key, data)))


@given(data=binary(), key=binary())
def test_encryption_randomness(data, key) -> None:
    e1 = encrypt(key, data)
    e2 = encrypt(key, data)
    assert e1 != e2
    assert decrypt(key, e1) == decrypt(key, e2)
