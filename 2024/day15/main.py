class Advent:
    def __init__(self, input_path):
        self.map = {}
        self.wide_map = {}
        self.start_pos = 0
        self.wide_start_pos = 0
        self.movements = []
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = file.readlines()

        map_lines = []
        wide_map_lines = []

        reading_map = True
        for line in lines:
            if line.strip() == "":
                reading_map = False
                continue

            if reading_map:
                map_lines.append(line.strip())
                wide_map_line = []
                for i in line.strip():
                    if i == "#":
                        wide_map_line += ["#", "#"]
                    elif i == "O":
                        wide_map_line += ["[", "]"]
                    elif i == ".":
                        wide_map_line += [".", "."]
                    elif i == "@":
                        wide_map_line += ["@", "."]
                wide_map_lines.append(wide_map_line)
            else:
                self.movements.extend(list(line.strip()))

        for row, line in enumerate(map_lines):
            for col, char in enumerate(line):
                pos = row + col * 1j
                if char == "@":
                    self.start_pos = pos
                self.map[pos] = char

        for row, line in enumerate(wide_map_lines):
            for col, char in enumerate(line):
                pos = row + col * 1j
                if char == "@":
                    self.wide_start_pos = pos
                self.wide_map[pos] = char

    def __print_map(self):
        max_row = int(max(key.real for key in self.map.keys())) + 1
        max_col = int(max(key.imag for key in self.map.keys())) + 1

        map = [[""] * max_col for _ in range(max_row)]

        for row in range(max_row):
            for col in range(max_col):
                map[row][col] = self.map[row + col * 1j]

        map_string = "\n".join(["".join(inner_list) for inner_list in map])
        print(map_string + "\n")

    def __gps(self, map, box):
        result = 0
        for char in map:
            if map[char] == box:
                coordinate = 100 * int(char.real) + int(char.imag)
                result += coordinate

        return result

    def __move(self, direction):
        boxes = []
        next_pos = self.start_pos + direction

        while self.map[next_pos] == "O":
            boxes.append(next_pos)
            next_pos += direction

        if self.map[next_pos] != "#":
            if len(boxes) > 0:
                self.map[self.start_pos] = "."
                self.map[boxes[0]] = "@"
                self.map[next_pos] = "O"
                self.start_pos = boxes[0]
            else:
                self.map[self.start_pos] = "."
                self.map[next_pos] = "@"
                self.start_pos = next_pos

    def __get_box(self, loc):
        if self.wide_map[loc] == "]":
            return (loc - 1j, loc)
        else:
            return (loc, loc + 1j)

    def __can_move(self, loc, direction, visited, boxes):
        if self.wide_map[loc] == "#":
            return False

        if self.wide_map[loc] == ".":
            return True

        box_loc = self.__get_box(loc)
        boxes.add(box_loc)
        visited.add(box_loc)

        for box_part in box_loc:
            box_loc_prime = self.__get_box(box_part + direction)
            if box_loc_prime not in visited:
                if not self.__can_move(box_part + direction, direction, visited, boxes):
                    return False

        return True

    def __wide_move(self, direction):
        next_pos = self.wide_start_pos + direction

        boxes = set()
        visited = set()
        can_move = self.__can_move(next_pos, direction, visited, boxes)

        if can_move:
            for box_loc in boxes:
                self.wide_map[box_loc[0]] = "."
                self.wide_map[box_loc[1]] = "."

            for box_loc in boxes:
                self.wide_map[box_loc[0] + direction] = "["
                self.wide_map[box_loc[1] + direction] = "]"
            self.wide_map[self.wide_start_pos] = "."
            self.wide_map[self.wide_start_pos + direction] = "@"
            self.wide_start_pos += direction

        return can_move

    def part_1(self):
        directions = {"^": -1, ">": 1j, "v": 1, "<": -1j}
        # self.__print_map()
        for movement in self.movements:
            self.__move(directions[movement])
            # self.__print_map()

        result = self.__gps(self.map, "O")

        return result

    def part_2(self):
        directions = {"^": -1, ">": 1j, "v": 1, "<": -1j}
        # self.__print_map()
        for movement in self.movements:
            self.__wide_move(directions[movement])
            # self.__print_map()

        result = self.__gps(self.wide_map, "[")

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
