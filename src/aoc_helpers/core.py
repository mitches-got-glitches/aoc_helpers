import collections
import inspect
import itertools
import re
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Any, Collection, Iterable, MutableSet

from .config import settings


def split_list(lst: list, val: Any):
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


def get_input_path():
    calling_module = inspect.stack()[1].filename
    input_file = "test_input.txt" if settings.test else "input.txt"
    return Path(calling_module).with_name(input_file)


def get_intersection(x: Collection[Any], y: Collection[Any]) -> MutableSet[Any]:
    """Get the set intersection of two collections."""
    return set(x).intersection(set(y))


# Use zip_longest from itertools to chunk the list up into groups of 3.
def group_elements(n: int, iterable: Iterable) -> list[list[int]]:
    """Group elements of a list into lists of size n."""
    return list(itertools.zip_longest(*[iter(iterable)] * n))


def union_all(sets: list[MutableSet[Any]]) -> MutableSet[Any]:
    """Union all sets in a list."""
    return reduce(lambda x, y: x.union(y), sets)


def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(itertools.islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


@dataclass
class RegexEqual(str):
    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)
        return self.match is not None


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(x, y):
    return x * y / gcd(x, y)
