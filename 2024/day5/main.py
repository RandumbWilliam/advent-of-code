class Advent:
    def __init__(self, input_path):
        self.rules = set()
        self.correct_pages = []
        self.incorrect_pages = []
        pages = self.__get_data(input_path)
        self.__check_pages(pages)

    def __check_pages(self, pages):
        for page in pages:
            page_set = set()
            for i in range(len(page)):
                for j in range(i + 1, len(page)):
                    page_set.add((page[i], page[j]))

            if page_set <= self.rules:
                self.correct_pages.append(page)
            else:
                self.incorrect_pages.append(page)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = file.readlines()

        pages = []
        empty_line = False
        for line in lines:
            line = line.strip()
            if not line:
                empty_line = True
                continue

            if not empty_line:
                if "|" in line:
                    x, y = map(int, line.split("|"))
                    self.rules.add((x, y))
            else:
                row = list(map(int, line.split(",")))
                pages.append(row)

        return pages

    def __calculate_total(self, pages):
        result = 0
        for page in pages:
            mid = (len(page) - 1) // 2
            result += page[mid]

        return result

    def part_1(self):
        result = self.__calculate_total(self.correct_pages)
        return result

    def part_2(self):
        fixed_pages = []
        for page in self.incorrect_pages:
            for i in range(len(page) - 1):
                j = i + 1
                while j < len(page):
                    if (page[i], page[j]) not in self.rules:
                        page[i], page[j] = page[j], page[i]
                    else:
                        j += 1
            fixed_pages.append(page)

        result = self.__calculate_total(fixed_pages)
        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
