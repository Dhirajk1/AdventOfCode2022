"""Day 12 Solution"""
import heapq
from typing import Callable
import sys


def solve(file_name: str):
    """Solves both parts"""
    parsed = [[char for char in line if char != "\n"] for line in open(file_name)]
    height, width = len(parsed), len(parsed[0])

    def get(curr: tuple[int, int]) -> int:
        """Converts a letter to elevation"""
        letter = parsed[curr[0]][curr[1]]
        if letter == "S":
            return ord("a")
        if letter == "E":
            return ord("z")
        return ord(letter)

    def add_neighbors(
        y: int,
        x: int,
        check: Callable,
        graph: dict[tuple[int, int], set[tuple[int, int]]],
    ):
        "Helper function to add neighbors to graph"
        neighbors = set()
        for point in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if (
                point[0] in range(height)
                and point[1] in range(width)
                and check((y, x), point)
            ):
                neighbors.add(point)
        graph[(y, x)] = neighbors

    # Populate graph and needed points
    graph1 = {}
    graph2 = {}
    S = (0, 0)
    E = (0, 0)
    for y in range(height):
        for x in range(width):
            if parsed[y][x] == "S":
                S = (y, x)
            if parsed[y][x] == "E":
                E = (y, x)
            add_neighbors(y, x, lambda start, end: get(end) <= get(start) + 1, graph1)
            add_neighbors(y, x, lambda start, end: get(start) <= get(end) + 1, graph2)

    def dijkstra(
        start: tuple[int, int],
        stop_when: Callable,
        graph: dict[tuple[int, int], set[tuple[int, int]]],
    ) -> dict[tuple[int, int], int]:
        """Dijkstra's algorithm to find the all the optimal paths"""
        dist = {pt: float("inf") for pt in graph}
        dist[start] = 0
        queue = []
        heapq.heappush(queue, (dist[start], start))

        while queue:
            pt = heapq.heappop(queue)[1]
            if stop_when(pt):
                return dist[pt]
            for neighbor in graph[pt]:
                new_path = dist[pt] + 1
                if new_path < dist[neighbor]:
                    dist[neighbor] = new_path
                    heapq.heappush(queue, (dist[neighbor], neighbor))
        return -1

    dists1 = dijkstra(S, lambda pt: pt == E, graph1)
    dists2 = dijkstra(E, lambda pt: get(pt) == ord("a"), graph2)
    return dists1, dists2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Give me the file plz :)")
    answer1, answer2 = solve(sys.argv[1])
    print(f"The answer to part one is {answer1}")
    print(f"The answer to part two in {answer2}")
