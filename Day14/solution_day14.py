"""Solution for Darow 14"""
import numpy as np

SAND = 2
WALL = 1


def solve(file_name: str) -> tuple[int, int]:
    """Solves both parts"""

    grid = np.zeros((200, 1000))
    bottom = 0

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
                    grid[start_row : end_row + 1, start_col : end_col + 1] = WALL
                    bottom = max(bottom, end_row)
                elif len(window) == 1:
                    col, row = points
                    grid[row, col] = WALL

    grid[bottom + 2] = WALL
    part1 = part2 = 0
    while grid[0, 500] != SAND:
        row, col = 0, 500
        while grid[row, col] != SAND:
            if not part1 and row == bottom:
                part1 = part2
            if not grid[row + 1, col]:
                row += 1
            elif not grid[row + 1, col - 1]:
                row += 1
                col -= 1
            elif not grid[row + 1, col + 1]:
                row += 1
                col += 1
            else:
                grid[row, col] = SAND
                part2 += 1

    return part1, part2


if __name__ == "__main__":
    answer1, answer2 = solve("input.txt")
    print(f"The answer to part one is {answer1}")
    print(f"The answer to part two is {answer2}")
