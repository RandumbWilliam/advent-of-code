import re


class Advent:
    def __init__(self, input_path):
        self.data = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            return file.read()

    def part_1(self):
        regex = r"mul\((-?\d+),(-?\d+)\)"
        matches = re.findall(regex, self.data)

        return sum(int(a) * int(b) for a, b in matches)

    def part_2(self):
        regex = r"mul\(-?\d+,-?\d+\)|do\(\)|don't\(\)"
        matches = re.findall(regex, self.data)

        current = "do()"
        result = 0
        for match in matches:
            if match == "do()" or match == "don't()":
                current = match
            else:
                if current == "do()":
                    a, b = re.findall(r"\d+", match)
                    result += int(a) * int(b)

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
