from itertools import chain
from functools import reduce
from operator import itemgetter, mul
from pathlib import Path

from advent_2023.utils import advent_header


def part_one() -> int:
    return sum(
        map(
            itemgetter(0),
            filter(
                lambda tup: tup[1]["red"] <= 12 and tup[1]["green"] <= 13 and tup[1]["blue"] <= 14,
                map(
                    lambda tup: (
                        tup[0], 
                        reduce(
                            lambda acc, el: acc | { (sp := el.split())[1]: max(acc[sp[1]], int(sp[0])) },
                            tup[1],
                            { "red": 0, "green": 0, "blue": 0 },
                        )
                    ),
                    map(
                        lambda tup: (tup[0], tuple(
                            chain.from_iterable(
                                map(
                                    lambda s: s.split(", "), 
                                    tup[1]
                                )
                            )
                        )),
                        map(
                            lambda tup: (int(tup[0].removeprefix("Game ")), tuple(tup[1].rstrip().split("; "))),
                            map(
                                lambda l: l.split(": ", maxsplit=1),
                                (Path(__file__).parent.parent/ "data" / "day2.txt")
                                    .open("r")
                                    .readlines()
                            )
                        )
                    )
                )
            )
        )
    )

def part_two() -> int:
    return sum(
        map(
            lambda tup: reduce(
                mul, tup[1].values(), 1
            ),
            map(
                lambda tup: (
                    tup[0], 
                    reduce(
                        lambda acc, el: acc | { (sp := el.split())[1]: max(acc[sp[1]], int(sp[0])) },
                        tup[1],
                        { "red": 0, "green": 0, "blue": 0 },
                    )
                ),
                map(
                    lambda tup: (tup[0], tuple(
                        chain.from_iterable(
                            map(
                                lambda s: s.split(", "), 
                                tup[1]
                            )
                        )
                    )),
                    map(
                        lambda tup: (int(tup[0].removeprefix("Game ")), tuple(tup[1].rstrip().split("; "))),
                        map(
                            lambda l: l.split(": ", maxsplit=1),
                            (Path(__file__).parent.parent/ "data" / "day2.txt")
                                .open("r")
                                .readlines()
                        )
                    )
                )
            )
        )
    )

if __name__ == "__main__":

    part_one_answer = part_one()
    part_two_answer = part_two()

    print(advent_header(2))
    print(f"{part_one_answer = }")
    print(f"{part_two_answer = }")