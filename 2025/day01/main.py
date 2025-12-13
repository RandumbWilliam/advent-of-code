import sys

def part1(input: str) -> None:
    sequence = []

    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            sequence.append((line[0], int(line[1:])));

    dial = 50
    password = 0
    for direction, steps in sequence:
        if direction == 'R':
            dial = (dial + steps) % 100
        elif direction == 'L':
            dial = (dial - steps) % 100

        if dial == 0:
            password += 1

    print(password)


def part2(input: str) -> None:
    sequence = []

    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            sequence.append((line[0], int(line[1:])));

    dial = 50
    password = 0
    for direction, steps in sequence:
        full, partial = divmod(steps, 100)
        password += full

        if direction == 'R':
            if dial + partial >= 100:
                password += 1
            dial = (dial + steps) % 100
        elif direction == 'L':
            if dial != 0 and dial - partial <= 0:
                password += 1
            dial = (dial - steps) % 100

    print(password)


def usage():
    print("Usage: python3 main.py <part1|part2> <input.txt>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    part = sys.argv[1]

    if part not in ["part1", "part2"]:
        usage()

    input = sys.argv[2]

    if part == "part1":
        part1(input)

    if part == "part2":
        part2(input)

