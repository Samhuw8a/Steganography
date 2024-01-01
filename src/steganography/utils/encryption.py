# Copied from https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python

import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from typing import Union

StringOrBytes = Union[str, bytes]


def encrypt(key: StringOrBytes, source: bytes, encode: bool = True) -> StringOrBytes:
    key = SHA256.new(key).digest()  # use SHA-256 to get a proper-sized AES key
    IV: bytes = Random.new().read(AES.block_size)  # type: ignore
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(
    key: StringOrBytes, rsource: StringOrBytes, decode: bool = True
) -> StringOrBytes:
    if decode:
        source = base64.b64decode(rsource.encode("latin-1"))  # type: ignore
    key = SHA256.new(key).digest()  # use SHA-256 to get a proper-sized AES key
    IV = source[: AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size :])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding
