"""ex05 - Listing to the Music."""

__author__ = "730239487"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even numbers in a list."""
    i: int = 0
    ys: list[int] = []
    while i < len(xs):
        test: int = xs[i] // 2
        if test == 0:
            ys.append(xs[i])
        i += 1
    return ys


def sub(bs: list[int]) -> list[int]:
    """Returns two random values from the list to provide a sample.""" 
    from random import randint
    cs: list[int] = []
    j: int = 0
    l: int = len(bs)
    while j < 2:
        k: int = randint(0, l)
        cs.append(bs[k])
        bs.pop(bs[k])
        j += 1
    return cs


def concat(cs: list[int], ds: list[int]) -> list[int]:
    """Puts two lists together into one."""
    es: list[int] = []
    m: int = 0
    while m < len(cs):
        es.append(cs[m])
        m += 1
    n: int = 0 
    while n < len(ds):
        es.append(ds[n])
        n += 1
    return es