"""Solution for Darow 14"""
import numpy as np


def solve(file_name: str) -> tuple[int, int]:
    """Solves both parts"""
    grid = np.zeros((200, 1000))
    limit = 0
    with open(file_name, "r") as file:
        for line in file:
            rock_ranges = line.strip().split("->")
            for i in range(len(rock_ranges)):
                window = rock_ranges[i : i + 2]
                points = [int(num) for point in window for num in point.split(",")]
                if len(window) == 2:
                    start_col, start_row, end_col, end_row = points
                    start_col, end_col = sorted([start_col, end_col])
                    start_row, end_row = sorted([start_row, end_row])
                    grid[start_row : end_row + 1, start_col : end_col + 1] = 1
                    limit = max(limit, end_row)
                elif len(window) == 1:
                    col, row = points
                    grid[row, col] = 1
    grid[limit + 2] = 1
    part1 = None
    col, row = 500, 0
    while grid[row, col] != 2:
        while grid[row + 1, col] == 0 or np.any(grid[row + 1, col - 1 : col + 2] == 0):
            row += 1
            if grid[row, col] == 0:
                continue
            elif grid[row, col - 1] == 0:
                col -= 1
            else:
                col += 1
            if not part1 and row == limit:
                part1 = (grid == 2).sum()
        grid[row, col] = 2
        col, row = 500, 0
    return part1, (grid == 2).sum()


if __name__ == "__main__":
    answer1, answer2 = solve("input.txt")
    print(f"The answer to part one is {answer1}")
    print(f"The answer to part two is {answer2}")
