from typing import Iterable
import pytest

from advent_2023.utils import prefixes, suffixes


def test_prefixes():
    assert list(map("".join, prefixes("ABC"))) == ["A", "AB", "ABC"]
    assert list(map(list.__call__, prefixes([1, 2, 3]))) == [[1], [1, 2], [1, 2, 3]]
    assert list(map(tuple.__call__, prefixes((1, 2, 3)))) == [(1,), (1, 2), (1, 2, 3)]


def test_suffixes():
    assert list(map("".join, suffixes("ABC"))) == ["C", "BC", "ABC"]
    assert list(map(list.__call__, suffixes([1, 2, 3]))) == [[3], [2, 3], [1, 2, 3]]
    assert list(map(tuple.__call__, suffixes((1, 2, 3)))) == [(3,), (2, 3), (1, 2, 3)]