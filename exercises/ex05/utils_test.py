"""ex05 Testing the Lists."""

__author__ = "730239487"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:  # tests that an empty list does not produce anything else
    xs: list[int] = []
    assert only_evens(xs) == []


def tests_only_evens_single() -> None:  # tests that an even integer is added
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_multi() -> None:  # tests that odd integers and multiple variables are added to the list
    xs: list[int] = [1, 2, 4, 8]
    assert only_evens(xs) == [2, 4, 8]


def test_sub_empty() -> None:  # tests that an empty list returns an empty list
    bs: list[int] = []
    assert sub(bs) == []


def test_sub_basic() -> None:  # tests than 2 variables are returened in either order
    bs: list[int] = [20, 30]
    assert sub(bs) == [20, 30] or [30, 20]


def test_sub_multi() -> None:  # tests that the function only returns 2 variables and that the two variables can be in any order
    bs: list[int] = [30, 40, 10, 20]
    assert sub(bs) == [20, 10] or [20, 30] or [20, 40] or [10, 20] or [10, 30] or [10, 40] or [30, 10] or [30, 20] or [30, 40] or [40, 10] or [40, 20] or [40, 30]


def test_concat_first() -> None:  # tests that the first list is added
    cs: list[int] = [20, 30]
    ds: list[int] = []
    assert concat(cs, ds) == [20, 30]


def test_concat_second() -> None:  # tests that the second list is added
    cs: list[int] = []
    ds: list[int] = [20, 30]
    assert concat(cs, ds) == [20, 30]


def test_concat_both() -> None:  # tests that the first list is added before the second list
    cs: list[int] = [30, 40, 50]
    ds: list[int] = [10, 20, 60]
    assert concat(cs, ds) == [30, 40, 50, 10, 20, 60]