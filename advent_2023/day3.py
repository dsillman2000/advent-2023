from pathlib import Path
from advent_2023.utils import advent_header, print_and_return

from more_itertools import ilen, triplewise
from itertools import chain, combinations, starmap, product, groupby, tee
from operator import itemgetter
import re


def part_one() -> int:

    return sum(
        chain.from_iterable(
            starmap(
                lambda symbols, middledigits: map(
                    lambda x: int(x[0][2]),
                    filter(
                        lambda linegb: any(
                            map(
                                lambda linegrp: linegb[0][0] - 1 <= linegrp[1] <= linegb[0][1],
                                linegb[1],
                            )
                        ),
                        groupby(
                            product(middledigits, symbols),
                            key=itemgetter(0),
                        )
                    )
                ),
                starmap(
                    lambda uppersymbols, middledigits, middlesymbols, lowersymbols: (
                        chain(
                            map(lambda x: x.span()[0], uppersymbols),
                            map(lambda x: x.span()[0], middlesymbols),
                            map(lambda x: x.span()[0], lowersymbols),
                        ),
                        map(lambda x: x.span() + (x.group(0),), middledigits),
                    ),
                    starmap(
                        lambda upper, middle, lower: (
                            re.finditer(r"[^0-9.]", upper.strip()), 
                            re.finditer(r"\d{1,3}", middle.strip()),
                            re.finditer(r"[^0-9.]", middle.strip()),
                            re.finditer(r"[^0-9.]", lower.strip()),
                        ),
                        triplewise(
                            [ 
                                (len((lines := (Path(__file__).parent.parent / "data" / "day3.txt")
                                    .open("r")
                                    .readlines())) - 1
                                ) * '.' + '\n' 
                            ] + 
                            lines + 
                            [(len(lines) - 1) * '.' + '\n']
                        )
                    )
                )
            )
        )
    )


def part_two() -> int:
    return sum(
        map(
            lambda digits: int(digits[0][1][2]) * int(digits[1][1][2]),
            chain.from_iterable(
                starmap(
                    lambda upperdigits, middlegears, middledigits, lowerdigits: filter(
                        lambda factors: len(factors) == 2 and iter(factors[0]),
                        map(
                            lambda tup: tuple(tup[1]),
                            groupby(
                                filter(
                                    lambda prod: prod[1][0] - 1 <= prod[0] <= prod[1][1],
                                    product(
                                        map(lambda x: x.span()[0], middlegears),
                                        chain(
                                            map(lambda x: x.span() + (x.group(0),), upperdigits),
                                            map(lambda x: x.span() + (x.group(0),), middledigits),
                                            map(lambda x: x.span() + (x.group(0),), lowerdigits),
                                        )
                                    )
                                ),
                                key = itemgetter(0),
                            )
                        )
                    ),
                    starmap(
                        lambda upper, middle, lower: (
                            re.finditer(r"\d{1,3}", upper.strip()), 
                            re.finditer(r"\*", middle.strip()),
                            re.finditer(r"\d{1,3}", middle.strip()),
                            re.finditer(r"\d{1,3}", lower.strip()),
                        ),
                        triplewise(
                            [ 
                                (len((lines := (Path(__file__).parent.parent / "data" / "day3.txt")
                                    .open("r")
                                    .readlines())) - 1
                                ) * '.' + '\n' 
                            ] + 
                            lines + 
                            [(len(lines) - 1) * '.' + '\n']
                        )
                    )
                )
            )
        )
    )


if __name__ == "__main__":

    part_one_answer = part_one()
    part_two_answer = part_two()

    print(advent_header(3))
    print(f"{part_one_answer = }")
    print(f"{part_two_answer = }")