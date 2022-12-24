"""Day 7 Solution"""
SIZE_LIMIT = 100000
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000


class Directory:
    """Directory Node"""

    def __init__(self, name, parent=None):
        self.name: str = name
        self.parent: Directory = parent
        self.children: dict[str, Directory] = dict()
        self.size: int = 0


def make_tree(file_name: str) -> Directory:
    """Converts file input to a tree"""
    root = Directory("/")
    curr = root
    for line in open(file_name, "r").readlines()[1:]:
        if line.startswith("$ cd"):
            name = line[5:-1]
            if name == "..":
                curr = curr.parent
            else:
                if name not in curr.children:
                    curr.children[name] = Directory(name, curr)
                curr = curr.children[name]
        elif not line.startswith(("$", "dir")):
            value = int(line[: line.index(" ")])
            curr.size += value
            parent = curr.parent
            while parent:
                parent.size += value
                parent = parent.parent
    return root


def solve(file_name: str):
    """Solves based on input"""
    root = make_tree(file_name)

    total_under_limit = 0
    need_to_free = SPACE_NEEDED - (TOTAL_SPACE - root.size)

    amount_freed = float("inf")
    stack = [root]
    while stack:
        directory = stack.pop()
        if directory.size <= SIZE_LIMIT:
            total_under_limit += directory.size
        if directory.size >= need_to_free and directory.size < amount_freed:
            amount_freed = directory.size
        for child in directory.children.values():
            stack.append(child)

    return total_under_limit, amount_freed


if __name__ == "__main__":
    answer1, answer2 = solve("input.txt")
    print(f"The answer for part one is {answer1}")
    print(f"The answer for part two is {answer2}")
