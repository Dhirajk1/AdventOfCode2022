"""Solution for Day 11"""
import re
from functools import reduce


class Monkey:
    """Monkey Class"""

    inspections = 0

    def __init__(self, lines: list[str]):
        for line in lines:
            if "Starting items" in line:
                split = re.split(" |, ", line)
                self.items = [int(num) for num in split[split.index("items:") + 1 :]]
            elif "Operation" in line:
                self.operation = line.strip().split("= old ")[1].split(" ")
            elif "Test" in line:
                self.test = int(line.split("by")[1])
            elif "true" in line:
                self.true_monkey = int(line.split("monkey ")[1])
            elif "false" in line:
                self.false_monkey = int(line.split("monkey ")[1])

    def do_operation(self, old: int, reduce_factor: int) -> int:
        """Update the worry level"""
        right = old if self.operation[1] == "old" else int(self.operation[1])
        worry = old + right if self.operation[0] == "+" else old * right
        return worry // reduce_factor

    def do_test(self, worry: int) -> bool:
        """Test divisibility"""
        return (worry % self.test) == 0

    def toss_to(self, worry: int) -> int:
        """Toss to next monkey"""
        self.items.pop(0)
        return self.true_monkey if self.do_test(worry) else self.false_monkey

    def move(self, reduce_factor) -> tuple[int, int]:
        """Make a move"""
        worry = self.do_operation(self.items[0], reduce_factor)
        self.inspections += 1
        return self.toss_to(worry), worry


def find_monkey_business(file_name: str, rounds: int, reduce_factor: int = 1) -> int:
    """Finds the monkey business"""
    monkeys = []

    with open(file_name, "r") as file:
        monkeys = []
        monkey_text = []
        for line in file:
            if line == "\n":
                monkeys.append(Monkey(monkey_text))
                monkey_text = []
            monkey_text.append(line)
        monkeys.append(Monkey(monkey_text))

    div_by = reduce(lambda product, m: product * m.test, monkeys, 1)

    def play_round():
        for monkey in monkeys:
            while monkey.items:
                next_monkey, worry = monkey.move(reduce_factor)
                monkeys[next_monkey].items.append(worry % div_by)

    for _ in range(rounds):
        play_round()

    inspection_cnt = [monkey.inspections for monkey in monkeys]
    highest = sorted(inspection_cnt)[-2:]
    return highest[0] * highest[1]


if __name__ == "__main__":
    answer1 = find_monkey_business("input.txt", 20, reduce_factor=3)
    print(f"The answer for part one is: {answer1}")
    answer2 = find_monkey_business("input.txt", 10000)
    print(f"The answer for part two is {answer2}")
