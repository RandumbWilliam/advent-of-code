class Advent:
    def __init__(self, input_path):
        self.map = {}
        self.antennas = {}
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(line.strip()) for line in file]

        for i, row in enumerate(lines):
            for j, value in enumerate(row):
                pos = i + j * 1j
                self.map[pos] = value
                if value != ".":
                    pos = i + j * 1j
                    if value not in self.antennas:
                        self.antennas[value] = []
                    self.antennas[value].append(pos)

    def part_1(self):
        antinodes = set()
        for frequency in self.antennas:
            positions = self.antennas[frequency]
            for i in range(len(positions) - 1):
                for j in range(i + 1, len(positions)):
                    pos1, pos2 = positions[i], positions[j]
                    antinode1 = 2 * pos1 - pos2
                    if antinode1 in self.map:
                        antinodes.add(antinode1)

                    antinode2 = 2 * pos2 - pos1
                    if antinode2 in self.map:
                        antinodes.add(antinode2)

        return len(antinodes)

    def part_2(self):
        antinodes = set()
        for frequency in self.antennas:
            positions = self.antennas[frequency]
            for i in range(len(positions) - 1):
                for j in range(i + 1, len(positions)):
                    pos1, pos2 = positions[i], positions[j]
                    dist = pos2 - pos1

                    curr_pos1 = pos1
                    while curr_pos1 in self.map:
                        antinodes.add(curr_pos1)
                        curr_pos1 += dist

                    curr_pos1 = pos1
                    while curr_pos1 in self.map:
                        antinodes.add(curr_pos1)
                        curr_pos1 -= dist

        return len(antinodes)


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
