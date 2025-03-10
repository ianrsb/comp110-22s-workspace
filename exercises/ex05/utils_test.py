"""ex05 Testing the Lists."""

__author__ = "730239487"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Tests that empty list is produced."""
    xs: list[int] = []
    assert only_evens(xs) == []


def tests_only_evens_single() -> None:
    """Tests than single variables is recorded."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_multi() -> None:
    """Tests that off integers are excluded and that multiple integers can be added."""
    xs: list[int] = [1, 2, 4, 8]
    assert only_evens(xs) == [2, 4, 8]


def test_sub_empty() -> None:
    """Tests that sub returns an empty list."""
    bs: list[int] = []
    assert sub(bs) == []


def test_sub_basic() -> None:
   """Tests that sub will return the proper variables."""
    bs: list[int] = [20, 30]
    assert sub(bs) == [20, 30] or [30, 20]


def test_sub_multi() -> None:
    """Test that a longer string returns any combination of the variables."""
    bs: list[int] = [30, 40, 10, 20]
    assert sub(bs) == [20, 10] or [20, 30] or [20, 40] or [10, 20] or [10, 30] or [10, 40] or [30, 10] or [30, 20] or [30, 40] or [40, 10] or [40, 20] or [40, 30]


def test_concat_first() -> None:
    """Tests that the function adds the first list."""
    cs: list[int] = [20, 30]
    ds: list[int] = []
    assert concat(cs, ds) == [20, 30]


def test_concat_second() -> None:
    """Tests that the function adds the second list"""
    cs: list[int] = []
    ds: list[int] = [20, 30]
    assert concat(cs, ds) == [20, 30]


def test_concat_both() -> None:
    """Tests that the first function is added and then the second function."""
    cs: list[int] = [30, 40, 50]
    ds: list[int] = [10, 20, 60]
    assert concat(cs, ds) == [30, 40, 50, 10, 20, 60]