import sys

def part1(input: str) -> None:
    banks = []
    with open(input, 'r') as file:
        for line in file:
            banks.append(line.strip())

    result = 0
    for bank in banks:
        l, r, pointer = 0, 1, 1 
        largest_joltage = int(bank[l] + bank[r])
        while pointer < len(bank):
            if int(bank[pointer]) > int(bank[l]) and pointer + 1 < len(bank):
                l = pointer
                r = pointer + 1
            elif int(bank[pointer]) > int(bank[r]):
                r = pointer

            joltage = int(bank[l] + bank[r])
            largest_joltage = max(joltage, largest_joltage)
            pointer += 1

        result += largest_joltage

    print(result)


def part2(input: str) -> None:
    banks = []
    with open(input, 'r') as file:
        for line in file:
            banks.append(line.strip())

    result = 0
    for bank in banks:
        largest_joltage = ''

        start_digit = 0
        for digits_left in range(12, 0 , -1):
            largest_battery = bank[start_digit]

            current_digit = start_digit

            while current_digit < len(bank):
                battery = bank[current_digit]
                if int(battery) > int(largest_battery) and current_digit + digits_left - 1 < len(bank):
                    largest_battery = battery
                    start_digit = current_digit

                current_digit += 1

            largest_joltage += largest_battery
            start_digit += 1

        result += int(largest_joltage)

    print(result)


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

