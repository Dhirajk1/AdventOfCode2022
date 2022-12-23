"""Day 10 Solution"""
from collections import deque


def solve(file_name: str, cycles_to_check: set) -> int:
    """Solves both parts of day 10"""
    # Loading in our operations
    operations = deque()  # (cycles, change)
    for line in open(file_name, "r").readlines():
        if "addx" in line:  # takes two cycles and adds
            operations.append([2, int(line.split(" ")[1])])
        else:  # one empty cycle
            operations.append([1, 0])

    # Running Operations
    signal_sum = 0
    X = cycle = 1
    display = [40 * [" "] for _ in range(6)]
    while operations:
        operations[0][0] -= 1
        x_pos = (cycle - 1) % 40
        if abs(X - x_pos) < 2:
            display[(cycle - 1) // 40][x_pos] = "█"
        if operations[0][0] == 0:
            X += operations[0][1]
            operations.popleft()
        cycle += 1
        if cycle in cycles_to_check:
            signal_sum += cycle * X
    return signal_sum, display


if __name__ == "__main__":
    answer1, answer2 = solve(
        file_name="input.txt", cycles_to_check={*range(20, 220 + 1, 40)}
    )
    print(f"The answer for part one is {answer1}")
    print("The answer for part two is:\n")
    print("\n".join("".join(row) for row in answer2))
