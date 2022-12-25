"""Solution for Day 13"""
from typing import Union
from ast import literal_eval
from functools import cmp_to_key, reduce
import numpy as np


def parse_file(file_name: str) -> list[list, list]:
    """Parses the file"""
    lines = open(file_name, "r").read().replace("\n\n", "\n").splitlines()
    packets = [literal_eval(line) for line in lines]
    pairs = [(packets[i], packets[i + 1]) for i in range(0, len(packets), 2)]
    return packets, pairs


def compare(a: Union[int, list], b: Union[int, list]) -> int:
    """Compares two elements are per the criteria"""
    if not isinstance(a, type(b)):  # cast to lists if they don't match
        if not isinstance(a, list):
            a = [a]
        else:
            b = [b]

    if isinstance(a, int):  # int comparison
        return np.sign(b - a)

    if isinstance(a, list):  # list comparison
        if comparison := next(
            (compare(x, y) for x, y in zip(a, b) if compare(x, y)), None
        ):  # check for any comparisons != 0
            return comparison
        return np.sign(len(b) - len(a))


def solve(file_name: str, dividers: list[list[list[int]]]) -> tuple[int, int]:
    """Solves both parts of day 13"""
    packets, pairs = parse_file(file_name)
    part1 = sum(i + 1 for i, pair in enumerate(pairs) if compare(*pair) == 1)

    part2_iter = sorted(packets + dividers, key=cmp_to_key(compare), reverse=True)
    part2 = reduce(
        lambda prod, divider: prod * (part2_iter.index(divider) + 1), dividers, 1
    )
    return part1, part2


if __name__ == "__main__":
    answer1, answer2 = solve("input.txt", dividers=[[[2]], [[6]]])
    print(f"The answer to part one is {answer1}")
    print(f"The answer to part two is {answer2}")
