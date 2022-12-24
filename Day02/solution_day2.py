"""Solution for Day 2"""


def get_score1(file_name: str) -> int:
    """Find the score for the game record"""
    score = 0
    convert = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    to_win = {1: 3, 2: 1, 3: 2}
    with open(file_name, "r") as file:
        for line in file:
            opp, you = [convert[move] for move in line.strip().split(" ")]
            score += you
            if you == opp:
                score += 3
            elif to_win[you] == opp:
                score += 6
    return score


def get_score2(file_name: str) -> int:
    """Get the score for the game record"""
    score = 0
    convert = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    to_lose = {1: 3, 2: 1, 3: 2}
    to_win = {1: 2, 2: 3, 3: 1}
    with open(file_name, "r") as file:
        for line in file:
            opp, result = line.strip().split(" ")
            opp = convert[opp]
            if result == "Y":  # draw
                score += 3 + opp
            if result == "X":  # loose
                score += to_lose[opp]
            if result == "Z":  # win
                score += 6 + to_win[opp]
    return score


if __name__ == "__main__":
    answer1 = get_score1("input.txt")
    print(f"The final score for part 1 is {answer1}")
    answer2 = get_score2("input.txt")
    print(f"The final score for part 2 is {answer2}")
