"""Solution for Day 5"""
import re


def parse(file_name: list[str]) -> tuple[list[list[str]], list[list[int]]]:
    """Parses the initial state and moves"""
    lines = open(file_name, "r").readlines()

    split_pt = lines.index("\n")
    initial_state, moves = lines[:split_pt], lines[split_pt + 1 :]
    moves = map(
        lambda move: [int(num) for num in re.split("move|from|to|\n", move) if num],
        moves,
    )

    stacks = int(initial_state[-1].split(" ")[-2])
    chunk_size = len(initial_state[0]) // stacks
    towers = [[] for _ in range(stacks)]

    for line in initial_state[:-1][::-1]:
        for group in range(stacks):
            parsed = line[chunk_size * group : chunk_size * group + chunk_size]
            if parsed[1] != " ":
                towers[group].append(parsed[1])

    return towers, moves


def make_moves1(file_name: str) -> str:
    """Makes moves according to situation 1"""
    towers, moves = parse(file_name)
    for amount, start, end in moves:
        for _ in range(amount):
            towers[end - 1].append(towers[start - 1].pop())
    return "".join(stack[-1] for stack in towers)


def make_moves2(file_name: str) -> str:
    """Makes moves according to situation 1"""
    towers, moves = parse(file_name)
    for amount, start, end in moves:
        towers[end - 1] += towers[start - 1][-amount:]
        del towers[start - 1][-amount:]
    return "".join(stack[-1] for stack in towers)


if __name__ == "__main__":
    answer1 = make_moves1("input.txt")
    print(f"Answer for part one: {answer1}")
    answer2 = make_moves2("input.txt")
    print(f"Answer for part two: {answer2}")
