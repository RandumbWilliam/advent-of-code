import numpy as np


class Advent:
    def __init__(self, input_path):
        self.map, self.start_pos = self.__get_data(input_path)
        self.visited_positions = set()

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(line.strip()) for line in file]

        map = np.array(lines)
        start_pos = np.argwhere(map == "^")[0]

        return map, start_pos

    def __is_loop(self, obstruction_position):
        if obstruction_position == (self.start_pos[0], self.start_pos[1]):
            return False

        self.map[obstruction_position] = "#"
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = self.map.shape

        visited = set()
        curr_direction = 0
        curr_x, curr_y = self.start_pos[0], self.start_pos[1]
        while (0 <= curr_x < rows) and (0 <= curr_y < cols):
            dx, dy = directions[curr_direction % 4]
            x_prime, y_prime = curr_x + dx, curr_y + dy
            is_inbound = (0 <= x_prime < rows) and (0 <= y_prime < cols)
            if is_inbound and self.map[x_prime, y_prime] == "#":
                curr_direction += 1
            else:
                position_direction = ((curr_x, curr_y), (dx, dy))
                if position_direction in visited:
                    self.map[obstruction_position] = "."
                    return True
                visited.add(position_direction)
                curr_x = x_prime
                curr_y = y_prime

        self.map[obstruction_position] = "."
        return False

    def part_1(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = self.map.shape

        curr_direction = 0
        curr_x, curr_y = self.start_pos[0], self.start_pos[1]
        while (0 <= curr_x < rows) and (0 <= curr_y < cols):
            dx, dy = directions[curr_direction % 4]
            x_prime, y_prime = curr_x + dx, curr_y + dy
            is_inbound = (0 <= x_prime < rows) and (0 <= y_prime < cols)
            if is_inbound and self.map[x_prime, y_prime] == "#":
                curr_direction += 1
            else:
                self.visited_positions.add((curr_x, curr_y))
                curr_x = x_prime
                curr_y = y_prime

        return len(self.visited_positions)

    def part_2(self):
        result = 0
        for position in self.visited_positions:
            is_loop = self.__is_loop(position)
            if is_loop:
                result += 1

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
