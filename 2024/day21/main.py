import sys
from heapq import heappop, heappush
from collections import deque


class Advent:
    def __init__(self, input_path):
        self.numeric_keypad = {
            "A": {"0", "3"},
            "0": {"A", "2"},
            "1": {"2", "4"},
            "2": {"0", "1", "3", "5"},
            "3": {"A", "2", "6"},
            "4": {"1", "5", "7"},
            "5": {"2", "4", "6", "8"},
            "6": {"3", "5", "9"},
            "7": {"4", "8"},
            "8": {"5", "7", "9"},
            "9": {"6", "8"}
        }
        self.directional_keypad = {
            "A": {"^", ">"},
            "^": {"A", "v"},
            "<": {"v"},
            ">": {"A", "v"}
        }
        self.codes = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            return [list(line.strip()) for line in file]

    def __dijkstra(self, source, graph):
        visited = {source}
        distance = {source: 0}
        pq = [(0, source)]

        while pq:
            dist, node = heappop(pq)
            visited.add(node)

            if distance[node] < dist:
                continue

            for neighbour in graph[node]:
                if neighbour in visited:
                    continue

                new_distance = distance.get(node, float("inf")) + 1
                if new_distance < distance.get(neighbour, float("inf")):
                    distance[neighbour] = new_distance
                    heappush(pq, (new_distance, neighbour))

        return distance

    def part_1(self):
        numeric_keypad_distances = {}
        for source in self.numeric_keypad:
            numeric_keypad_distances[source] = self.__dijkstra(source, self.numeric_keypad)

        directional_keypard_distances = {}
        for source in self.directional_keypad:
            directional_keypard_distances[source] = self.__dijkstra(source, self.directional_keypad)


        return

    def part_2(self):
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Syntax:")
        print("    python main.py <file.txt>")
        exit()

    input_file = sys.argv[1]
    advent = Advent(input_file)
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)


