class Advent:
    def __init__(self, input_path):
        self.machines = []
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = file.readlines()

        for i in range(0, len(lines), 4):
            button_a = lines[i].strip()
            button_b = lines[i + 1].strip()
            prize = lines[i + 2].strip()

            # Parse values from the lines
            a_x = int(button_a.split("X+")[1].split(",")[0])
            a_y = int(button_a.split("Y+")[1])
            b_x = int(button_b.split("X+")[1].split(",")[0])
            b_y = int(button_b.split("Y+")[1])
            prize_x = int(prize.split("X=")[1].split(",")[0])
            prize_y = int(prize.split("Y=")[1])

            # Create the tuples and add to the result
            x_tuple = (a_x, b_x, prize_x)
            y_tuple = (a_y, b_y, prize_y)
            self.machines.append((x_tuple, y_tuple))

    def part_1(self):
        tokens = 0
        for machine in self.machines:
            A11 = machine[0][0]
            A12 = machine[0][1]
            A21 = machine[1][0]
            A22 = machine[1][1]
            b1 = machine[0][2]
            b2 = machine[1][2]

            # Step 1: Calculate the determinant of A
            det_A = A11 * A22 - A12 * A21

            # Step 2: Calculate the determinant of A1 (replace the first column of A with b)
            det_A1 = b1 * A22 - A12 * b2

            # Step 3: Calculate the determinant of A2 (replace the second column of A with b)
            det_A2 = A11 * b2 - A21 * b1

            # Step 4: Solve for x1 and x2 using Cramer's rule
            if det_A == 0:
                return "The system has no unique solution (determinant is 0)."

            if det_A1 % det_A == 0 and det_A2 % det_A == 0:
                x1 = det_A1 // det_A
                x2 = det_A2 // det_A
                tokens += 3 * x1 + x2

        return tokens

    def part_2(self):
        what = 10000000000000
        tokens = 0
        for machine in self.machines:
            A11 = machine[0][0]
            A12 = machine[0][1]
            A21 = machine[1][0]
            A22 = machine[1][1]
            b1 = machine[0][2] + what
            b2 = machine[1][2] + what

            # Step 1: Calculate the determinant of A
            det_A = A11 * A22 - A12 * A21

            # Step 2: Calculate the determinant of A1 (replace the first column of A with b)
            det_A1 = b1 * A22 - A12 * b2

            # Step 3: Calculate the determinant of A2 (replace the second column of A with b)
            det_A2 = A11 * b2 - A21 * b1

            # Step 4: Solve for x1 and x2 using Cramer's rule
            if det_A == 0:
                return "The system has no unique solution (determinant is 0)."

            if det_A1 % det_A == 0 and det_A2 % det_A == 0:
                x1 = det_A1 // det_A
                x2 = det_A2 // det_A
                tokens += 3 * x1 + x2

        return tokens


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
