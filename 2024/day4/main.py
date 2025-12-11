import numpy as np


class Advent:
    def __init__(self, input_path):
        self.data = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            return [list(line.strip()) for line in file]

    def __count_xmas(self, data):
        result = 0
        row = data[0]
        s = "".join(row)
        if s == "XMAS" or s[::-1] == "XMAS":
            result += 1

        col = data[:, 0]
        s = "".join(col)
        if s == "XMAS" or s[::-1] == "XMAS":
            result += 1

        diag = data.diagonal()
        s = "".join(diag)
        if s == "XMAS" or s[::-1] == "XMAS":
            result += 1

        flip_diag = np.fliplr(data).diagonal()
        s = "".join(flip_diag)
        if s == "XMAS" or s[::-1] == "XMAS":
            result += 1

        return result

    def part_1(self):
        data = np.array(self.data)
        row, col = data.shape
        result = 0
        for i in range(row):
            for j in range(col):
                scope = data[i : i + 4, j : j + 4]
                result += self.__count_xmas(scope)

        return result

    def part_2(self):
        data = np.array(self.data)
        row, col = data.shape
        result = 0
        for i in range(row):
            for j in range(col):
                scope = data[i : i + 3, j : j + 3]
                diag = scope.diagonal()
                d = "".join(diag)
                flip_diag = np.fliplr(scope).diagonal()
                f = "".join(flip_diag)
                if (d == "MAS" or d[::-1] == "MAS") and (
                    f == "MAS" or f[::-1] == "MAS"
                ):
                    result += 1

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
