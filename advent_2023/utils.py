from operator import neg
from typing import Iterable, TypeVar
from itertools import repeat, accumulate, islice, starmap
from more_itertools import ilen


def advent_header(day: int) -> str:
    return "=" * 40 + f" Advent of Code 2023 - Day {day} " + "=" * 40

T = TypeVar("T")
def print_and_return(value: T) -> T:
    print(value)
    return value
    


def prefixes(iterable: Iterable[T]) -> Iterable[T]:
    return starmap(
        islice.__call__, 
        zip(
            repeat(iterable), 
            repeat(None), 
            range(1, ilen(iterable) + 1),
        ),
    )

def suffixes(iterable: Iterable[T]) -> Iterable[T]:
    return starmap(
        islice.__call__, 
        zip(
            repeat(iterable), 
            reversed(range(0, ilen(iterable))),
            repeat(None),
        ),
    )
