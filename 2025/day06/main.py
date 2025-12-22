import sys

def part1(input: str) -> None:
    sheet = []
    with open(input, 'r') as file:
        for line in file:
            sheet.append(line.strip().split())

    operators = sheet.pop()

    answers = []

    for operator in operators:
        if operator == '+':
            answers.append(0)
        if operator == '*':
            answers.append(1)

    for row in sheet:
        for j, number in enumerate(row):
            if operators[j] == '+':
                answers[j] += int(number)
            if operators[j] == '*':
                answers[j] *= int(number)

    result = sum(answers)

    print(result)


def part2(input: str) -> None:
    sheet = []
    with open(input, 'r') as file:
        for line in file:
            sheet.append(line.rstrip('\n'))

    operators = sheet.pop().split()

    problems = []
    problem = []
    for j in range(len(sheet[0]) - 1, -1, -1):
        number = ''
        for i in range(len(sheet)):
            digit = sheet[i][j]
            number += digit

        if number.strip() != '':
            problem.append(int(number))
        else:
            problems.append(problem)
            problem = []

    if problem:
        problems.append(problem)

    result = 0
    for problem in problems:
        operator = operators.pop()

        answer = 0
        if operator == '*':
            answer = 1

        for value in problem:
            if operator == '+':
                answer += value
            if operator == '*':
                answer *= value

        result += answer

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


