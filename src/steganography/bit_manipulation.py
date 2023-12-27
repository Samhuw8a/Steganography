def set_bit(org: int, n: int, new: int) -> int:
    """set the n'th bit of org to new (copied from: https://github.com/livz/cloacked-pixel/blob/master/lsb.py#L43)"""
    mask = 1 << n
    org &= ~mask
    if new:
        n |= mask
    return org
