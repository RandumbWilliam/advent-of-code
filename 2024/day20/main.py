import sys
from collections import deque


class Advent:
    def __init__(self, input_path):
        self.map = {}
        self.start = (0,0)
        self.end = (0,0)
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(line.strip()) for line in file]

        for i, row in enumerate(lines):
            for j, value in enumerate(row):
                pos = (i, j)
                if value == "S":
                    self.start = pos
                if value == "E":
                    self.end = pos
                self.map[pos] = value

    def __get_path(self):
        r, c = self.start
        path = {self.start: 0}
        
        while (r, c) != self.end:
            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if (nr, nc) in path:
                    continue

                if (nr, nc) not in self.map:
                    continue

                if self.map[(nr, nc)] == "#":
                    continue

                path[(nr, nc)] = path[(r, c)] + 1
                r, c = nr, nc

        return path

    def part_1(self):
        path = self.__get_path()

        result = 0
        cheats = {}
        for (r, c), ps in path.items():
            for nr, nc in [(r - 2, c), (r, c + 2), (r + 2, c), (r, c - 2)]:
                if (nr, nc) not in self.map:
                    continue

                if self.map[(nr, nc)] == "#":
                    continue

                if (nr, nc) not in path:
                    continue

                save = path[(nr, nc)] - ps - 2
                if save > 0:
                    cheats[save] = cheats.get(save, 0) + 1
                    if save >= 100:
                        result += 1

        return result

    def part_2(self):
        path = self.__get_path()

        result = 0
        cheats = {}
        for (r, c), ps in path.items():
            # Manhattan distance = |x1 - x2| + |y1 - y2|
            for dr in range(-20, 21):
                for dc in range(-20 + abs(dr), 20 - abs(dr) + 1):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in self.map:
                        continue

                    if self.map[(nr, nc)] == "#":
                        continue

                    if (nr, nc) not in path:
                        continue

                    save = path[(nr, nc)] - ps - abs(dr) - abs(dc)
                    if save >= 50:
                        cheats[save] = cheats.get(save, 0) + 1
                        if save >= 100:
                            result += 1

        return result

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

