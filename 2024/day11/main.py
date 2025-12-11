from collections import defaultdict


class Advent:
    def __init__(self, input_path):
        self.stones = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            data = file.read()

        return [int(x) for x in data.split()]

    def __blink(self, stones):
        new_stones = defaultdict(int)
        for stone in stones:
            l = len(str(stone))
            if stone == 0:
                new_stones[1] += stones[0]
            elif l % 2 == 0:
                new_stones[int(str(stone)[l // 2 :])] += stones[stone]
                new_stones[int(str(stone)[: l // 2])] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]

        return new_stones

    def part_1(self):
        new_stones = defaultdict(int)
        for stone in self.stones:
            new_stones[stone] += 1

        for _ in range(25):
            new_stones = self.__blink(new_stones)

        result = 0
        for stone in new_stones:
            result += new_stones[stone]

        return result

    def part_2(self):
        new_stones = defaultdict(int)
        for stone in self.stones:
            new_stones[stone] += 1

        for _ in range(75):
            new_stones = self.__blink(new_stones)

        result = 0
        for stone in new_stones:
            result += new_stones[stone]

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
