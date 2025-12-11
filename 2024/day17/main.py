import sys
import re


class Advent:
    def __init__(self, input_path):
        self.a, self.b, self.c, *self.program = map(int, re.findall(r"\d+", open(input_path).read()))

    def __combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        else:
            raise RuntimeError("invalid combo operand", operand)


    def part_1(self):
        pointer = 0
        output = []
        
        while pointer < len(self.program):
            ins = self.program[pointer]
            operand = self.program[pointer + 1]

            if ins == 0:
                self.a = self.a >> self.__combo(operand)
            elif ins == 1:
                self.b = self.b ^ operand
            elif ins == 2:
                self.b = self.__combo(operand) % 8
            elif ins == 3:
                if self.a != 0:
                    pointer = operand
                    continue
            elif ins == 4:
                self.b = self.b ^ self.c
            elif ins == 5:
                output.append(self.__combo(operand) % 8)
            elif ins == 6:
                self.b = self.a >> self.__combo(operand)
            elif ins == 7:
                self.c = self.a >> self.__combo(operand)

            pointer += 2

        return ",".join(map(str, output))

    def part_2(self):
        def find(program, ans):
            if len(program) == 0:
                return ans

            for i in range(8):
                a = ans >> 3 | i
                b = a % 8
                b = b ^ 5
                c = a >> b
                b = b ^ 6
                b = b ^ c
                if b % 8 == program[-1]:
                    sub = find(program[:-1], a)
                    if sub is None:
                        continue
                    return sub

        return find(self.program, 0)

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

