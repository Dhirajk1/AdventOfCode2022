"""Solution for Day 3"""


def get_priority(char: str) -> int:
    """Gets priority for a character"""
    if char <= "Z":
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


def find_priority_sum1(file_name: str) -> int:
    """Find the sum of prority given a file"""
    total = 0
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            n = len(line)
            right, left = line[: n // 2], line[n // 2 :]
            common = set(right) & set(left)
            total += get_priority(*common)
    return total


def find_priority_sum2(file_name: str, per_group: int) -> int:
    """Find the sum of prority given a file"""
    total = 0
    with open(file_name, "r") as file:
        lines = file.readlines()
        for group in range(0, len(lines), per_group):
            common = {chr(i) for i in range(ord("A"), ord("z") + 1)}
            for elf in range(per_group):
                common &= set(lines[group + elf].strip())
            total += get_priority(*common)
    return total


if __name__ == "__main__":
    answer1 = find_priority_sum1("input.txt")
    print(f"The total priority for part one is {answer1}")
    answer2 = find_priority_sum2("input.txt", 3)
    print(f"The total priority for part two is {answer2}")
