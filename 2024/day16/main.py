import sys
from collections import deque
from heapq import heappop, heappush


class Advent:
    def __init__(self, input_path):
        self.map = {}
        self.start = (0,0)
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(line.strip()) for line in file]

        for i, row in enumerate(lines):
            for j, value in enumerate(row):
                pos = (i,j)
                if value == "S":
                    self.start = pos
                self.map[pos] = value

    def __dijkstra(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        pq = [(0, *self.start, 0, 1, [self.start])]
        best_cost = float("inf")
        visited = set()
        distances = {(*self.start, 0, 1): 0}
        tiles = set()

        while pq:
            cost, r, c, dr, dc, path = heappop(pq)
            visited.add((r, c, dr, dc))

            if self.map[(r,c)] == "E":
                if cost > best_cost:
                    break
                best_cost = cost 
                for tile in path:
                    tiles.add(tile)

            for ndr, ndc in directions:
                nr, nc = r + ndr, c + ndc

                if (nr, nc, ndr, ndc) in visited:
                    continue
                
                if self.map[(nr, nc)] == "#":
                    continue

                new_cost = cost + (1 if (ndr, ndc) == (dr, dc) else 1001)
                if new_cost <= distances.get((nr, nc, ndr, ndc), float("inf")):
                    distances[(nr, nc, ndr, ndc)] = new_cost
                    heappush(pq, (new_cost, nr, nc, ndr, ndc, path + [(nr, nc)]))

        return best_cost, len(tiles)

    def part_1(self):
        score, _= self.__dijkstra()

        return score

    def part_2(self):
        _, tiles = self.__dijkstra()

        return tiles


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
