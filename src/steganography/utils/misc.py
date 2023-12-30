from typing import Callable

__all__ = ["HashFunction", "test"]

HashFunction = Callable[[bytes], str]
