from functools import reduce
from pathlib import Path
from itertools import tee, dropwhile, starmap, repeat
from more_itertools import sliding_window, minmax
from operator import add, itemgetter

from advent_2023.utils import *

def part_one() -> int:
    return sum(
        map(
            int,
            starmap(
                add,
                map(
                    lambda t: (
                        next(
                            dropwhile(
                                lambda c: not c.isdigit(),
                                t[0],
                            )
                        ),
                        next(
                            dropwhile(
                                lambda c: not c.isdigit(),
                                reversed(t[1]),
                            )
                        ),
                    ),
                    zip(
                        *tee(
                            (Path(__file__).parent.parent / "data" / "day1.txt")
                                .open("r")
                                .readlines(),
                            2
                        )
                    ),
                )
            ),
        )
    )

def part_two() -> int:
    return sum(
        map(
            int,
            map(
                lambda concat: concat
                    .replace("one", "1")
                    .replace("two", "2")
                    .replace("three", "3")
                    .replace("four", "4")
                    .replace("five", "5")
                    .replace("six", "6")
                    .replace("seven", "7")
                    .replace("eight", "8")
                    .replace("nine", "9"),
                starmap(
                    add,
                    map(
                        lambda line: (
                            sorted(
                                list(
                                    filter(
                                        lambda tup: tup[0] >= 0,
                                        map(
                                            lambda tup: (tup[1].find(tup[0]), tup[0]),
                                            zip(
                                                (
                                                    "1", "one", "2", "two", "3", "three", "4", "four", "5", "five",
                                                    "6", "six", "7", "seven", "8", "eight", "9", "nine",
                                                ),
                                                repeat(line),
                                            ),
                                        )
                                    ),
                                ),
                                key = itemgetter(0),
                            )[0][1],
                            sorted(
                                list(
                                    filter(
                                        lambda tup: tup[0] >= 0,
                                        map(
                                            lambda tup: (tup[1].rfind(tup[0]), tup[0]),
                                            zip(
                                                (
                                                    "1", "one", "2", "two", "3", "three", "4", "four", "5", "five",
                                                    "6", "six", "7", "seven", "8", "eight", "9", "nine",
                                                ),
                                                repeat(line),
                                            ),
                                        )
                                    ),
                                ),
                            )[-1][1],
                        ),
                        (Path(__file__).parent.parent / "data" / "day1.txt")
                            .open("r")
                            .readlines(),
                    ),
                ),
            ),
        )
    )
    
if __name__ == "__main__":

    part_one_answer = part_one()
    part_two_answer = part_two()

    print(advent_header(1))
    print(f"{part_one_answer = }")
    print(f"{part_two_answer = }")