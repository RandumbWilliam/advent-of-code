import sys


class Advent:
    def __init__(self, input_path):
        self.available_towels = set()
        self.designs = []
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            content = file.read().strip()
            data = content.split("\n\n")
            self.available_towels = set(data[0].split(", "))
            self.designs = data[1].split("\n")

    def part_1(self):
        cache = {}
        def is_possible(design):
            if design == "":
                return True
            if design in cache:
                return cache[design]

            for i in range(len(design) + 1):
                if design[:i] in self.available_towels:
                    if is_possible(design[i:]):
                        cache[design] = True
                        return True
            
            cache[design] = False
            return False

        possible_designs = 0
        for design in self.designs:
            if is_possible(design):
                possible_designs += 1
        return possible_designs

    def part_2(self):
        cache = {}
        def possibilities(design):
            if design == "":
                return 1
            if design in cache:
                return cache[design]

            count = 0
            for i in range(len(design) + 1):
                if design[:i] in self.available_towels:
                    count += possibilities(design[i:])
                    cache[design] = count
            
            return count

        possible_designs = 0
        for design in self.designs:
            possible_designs += possibilities(design)
        return possible_designs

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

