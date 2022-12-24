"""Solution for Day 6"""


def find_packet_marker(msg: str, char_num: int) -> int:
    """Find the index of the start of packet marker"""
    for idx in range(len(msg) - char_num):
        if len(set(msg[idx : idx + char_num])) == char_num:
            return idx + char_num
    return -1


if __name__ == "__main__":
    prompt = open("input.txt").readline()
    print(f"The answer for part one is: {find_packet_marker(prompt, 4)}")
    print(f"The answer for part two is {find_packet_marker(prompt, 14)}")
