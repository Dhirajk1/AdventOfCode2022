"""
Solution for Day 1
"""
import numpy as np


def solve1(file_name: str) -> int:
    """Solves problem from the file input"""
    res = 0
    with open(file_name, "r") as file:
        curr_sum = 0
        for line in file:
            if line != "\n":
                curr_sum += int(line)
            else:
                res = max(res, curr_sum)
                curr_sum = 0
    res = max(res, curr_sum)
    return res


def solve2(file_name: str, num_largest: int) -> int:
    """Solves problem from the file input"""
    highest = np.zeros(num_largest).astype(int)
    min_idx = np.argmin(highest)

    with open(file_name, "r") as file:
        curr_sum = 0
        for line in file:
            if line != "\n":
                curr_sum += int(line)
            else:
                if curr_sum > highest[min_idx]:
                    highest[min_idx] = curr_sum
                    min_idx = np.argmin(highest)
                curr_sum = 0
    if curr_sum > highest[min_idx]:
        highest[min_idx] = curr_sum

    return highest.sum()


if __name__ == "__main__":
    answer1 = solve1("input.txt")
    print(f"The answer for part 1 is {answer1} calories")
    answer2 = solve2("input.txt", 3)
    print(f"The answer for part 2 is {answer2} calories")
