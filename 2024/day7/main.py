import math


class Advent:
    def __init__(self, input_path):
        self.targets, self.values = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = file.readlines()

        targets = []
        values = []
        for line in lines:
            target, value = line.strip().split(":")
            targets.append(int(target.strip()))
            values.append([int(v) for v in value.split()])

        return targets, values

    def __get_operations(self, depth, operations):
        result = []

        def backtrack(i, combination):
            if i == depth:
                result.append(combination)
                return

            for operation in operations:
                backtrack(i + 1, combination + [operation])

        backtrack(0, [])

        return result

    def part_1(self):
        calibration_result = 0
        for i in range(len(self.targets)):
            target = self.targets[i]
            values = self.values[i]

            operations = self.__get_operations(len(values) - 1, ["*", "+"])
            for operation in operations:
                result = values[0]
                for j in range(len(operation)):
                    if operation[j] == "+":
                        result += values[j + 1]
                    elif operation[j] == "*":
                        result *= values[j + 1]

                if result == target:
                    calibration_result += target
                    break

        return calibration_result

    def part_2(self):
        calibration_result = 0
        for i in range(len(self.targets)):
            target = self.targets[i]
            values = self.values[i]

            operations = self.__get_operations(len(values) - 1, ["*", "+", "||"])
            for operation in operations:
                result = values[0]
                for j in range(len(operation)):
                    if operation[j] == "+":
                        result += values[j + 1]
                    elif operation[j] == "*":
                        result *= values[j + 1]
                    elif operation[j] == "||":
                        value_digits = int(math.log10(values[j + 1])) + 1
                        result = result * (10**value_digits) + values[j + 1]

                if result == target:
                    calibration_result += target
                    break

        return calibration_result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
