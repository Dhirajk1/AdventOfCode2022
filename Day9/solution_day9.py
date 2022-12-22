"""Solution for Day 9"""
import numpy as np

BOARD_LIMIT = 1000


def parse_move(move: str) -> np.ndarray:
    """Gives the change in position for move"""
    direction, amount = move.split(" ")
    amount = int(amount)
    if direction == "U":
        return np.array([-amount, 0])
    if direction == "R":
        return np.array([0, amount])
    if direction == "D":
        return np.array([amount, 0])
    if direction == "L":
        return np.array([0, -amount])


def count_tail_positions(file_name: str, knots: int) -> int:
    """Counts all the positions the tail has visited"""
    visited = np.zeros((BOARD_LIMIT, BOARD_LIMIT)).astype(int)
    rope_pos = np.ones((knots, 2)).astype(int) * BOARD_LIMIT // 2

    def make_move(rope_pos: np.ndarray, knot: int = 1):
        """Updates the knots so they follow eachother"""
        if knot < len(rope_pos):
            diff = rope_pos[knot - 1] - rope_pos[knot]
            while any(abs(diff) > 1):
                rope_pos[knot] += np.sign(diff)
                if knot == len(rope_pos) - 1:  # keep track of tail
                    visited[rope_pos[-1, 0], rope_pos[-1, 1]] = 1
                make_move(rope_pos, knot + 1)
                diff = rope_pos[knot - 1] - rope_pos[knot]

    visited[BOARD_LIMIT // 2, BOARD_LIMIT // 2] = 1
    for line in open(file_name, "r").readlines():
        rope_pos[0] += parse_move(line)  # move head
        make_move(rope_pos)  # move rest
    return visited.sum()


if __name__ == "__main__":
    print(f"The answer for part one is {count_tail_positions('input.txt', 2)}")
    print(f"The answer for part two is {count_tail_positions('input.txt', 10)}")
