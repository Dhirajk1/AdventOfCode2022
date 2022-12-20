"""Day 4 Solution"""

import re


def is_total_subset(line: str) -> bool:
    """Check if the line is a subset"""
    first_start, first_end, second_start, second_end = (
        int(num) for num in re.split(",|-", line)
    )
    return (first_start - second_start) * (second_end - first_end) >= 0


def find_all_subsets1(file_name: str) -> int:
    """Count all the pairs where ranges are subsets"""
    return sum(is_total_subset(line) for line in open(file_name, "r").readlines())


def is_any_subset(line: str) -> bool:
    "Find whether the ranges have any overlap"
    first_start, first_end, second_start, second_end = (
        int(num) for num in re.split(",|-", line)
    )
    return (first_start - second_end) * (second_start - first_end) >= 0


def find_all_subsets2(file_name: str) -> int:
    "Count the number of pairs where ranges have overlap"
    return sum(is_any_subset(line) for line in open(file_name, "r").readlines())


if __name__ == "__main__":
    answer1 = find_all_subsets1("input.txt")
    print(f"Part one answer: {answer1}")
    answer2 = find_all_subsets2("input.txt")
    print(f"Part two answer: {answer2}")
