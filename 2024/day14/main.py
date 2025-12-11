from collections import defaultdict


class Advent:
    def __init__(self, input_path):
        self.robots = []
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            p_part, v_part = line.strip().split()
            px, py = map(int, p_part[2:].split(","))
            vx, vy = map(int, v_part[2:].split(","))

            self.robots.append([px + py * 1j, vx + vy * 1j])

    def part_1(self, seconds, size):
        new_positions = defaultdict(int)
        for robot in self.robots:
            new_position = robot[0] + robot[1] * seconds
            new_position_x = new_position.real % size[0]
            new_position_y = new_position.imag % size[1]
            new_positions[(new_position_x + new_position_y * 1j)] += 1

        quadrants = [0, 0, 0, 0]
        for position in new_positions:
            if position.real < size[0] // 2 and position.imag > size[1] // 2:
                quadrants[0] += new_positions[position]
            elif position.real > size[0] // 2 and position.imag > size[1] // 2:
                quadrants[1] += new_positions[position]
            elif position.real < size[0] // 2 and position.imag < size[1] // 2:
                quadrants[2] += new_positions[position]
            elif position.real > size[0] // 2 and position.imag < size[1] // 2:
                quadrants[3] += new_positions[position]

        result = 1
        for quadrant in quadrants:
            result *= quadrant

        return result

    def part_2(self, size):
        open("positions.txt", "w+").close()
        file = open("positions.txt", "a")

        robots = self.robots.copy()
        seen = set()

        max_counter = 0
        while max_counter < 20000:
            map = [["."] * size[0] for _ in range(size[1])]
            for index, robot in enumerate(robots):
                x = int(robot[0].real)
                y = int(robot[0].imag)

                map[y][x] = "#"
                new_position = robot[0] + robot[1]
                new_position_x = new_position.real % size[0]
                new_position_y = new_position.imag % size[1]
                robots[index][0] = new_position_x + new_position_y * 1j

            map_string = "\n".join(["".join(inner_list) for inner_list in map])

            if map_string in seen:
                print(f"number of possible positions: {max_counter}")
                break
            seen.add(map_string)

            file.write(f"{max_counter}\n")
            file.write(map_string + "\n")
            file.write("\n")

            max_counter += 1

        return


if __name__ == "__main__":
    seconds = 100
    size = (101, 103)
    size_test = (11, 7)
    advent = Advent("input.txt")
    part_1 = advent.part_1(seconds, size)
    part_2 = advent.part_2(size)

    print(part_1)
    print(part_2)
