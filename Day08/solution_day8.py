"""Solution for Day 8"""
import numpy as np


def count_visible(data: np.ndarray) -> int:
    """Solves for the total trees visible"""
    seen = np.zeros_like(data)
    rows, cols = seen.shape

    def check(row, col, curr_highest):
        if data[row, col] > curr_highest[0]:
            curr_highest[0] = data[row, col]
            seen[row, col] = 1

    # down
    for col in range(cols):
        curr_highest = [-1]
        for row in range(rows):
            check(row, col, curr_highest)
    # up
    for col in range(cols):
        curr_highest = [-1]
        for row in reversed(range(rows)):
            check(row, col, curr_highest)
    # left
    for row in range(rows):
        curr_highest = [-1]
        for col in range(cols):
            check(row, col, curr_highest)
    # right
    for row in range(rows):
        curr_highest = [-1]
        for col in reversed(range(cols)):
            check(row, col, curr_highest)

    return seen.sum()


def find_most_scenic(data: np.ndarray) -> int:
    """Find the most scenic tree's score"""
    scores = np.ones_like(data)
    rows, cols = scores.shape

    def count_trees(path, limit):
        count = 0
        for tree in path:
            count += 1
            if tree >= limit:
                break
        return count

    for row in range(rows):
        for col in range(cols):
            val = data[row, col]
            # up
            scores[row, col] *= count_trees(data[:row, col][::-1], val)
            # left
            scores[row, col] *= count_trees(data[row, :col][::-1], val)
            # down
            scores[row, col] *= count_trees(data[row + 1 :, col], val)
            # right
            scores[row, col] *= count_trees(data[row, col + 1 :], val)

    return scores.max()


if __name__ == "__main__":
    lines = open("input.txt", "r").readlines()
    input_data = np.array([[int(num) for num in line.strip()] for line in lines])
    print(f"The answer for part one is {count_visible(input_data)}")
    print(f"The answer for part two is {find_most_scenic(input_data)}")
