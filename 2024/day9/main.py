class Advent:
    def __init__(self, input_path):
        self.disk_map = self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            return file.read().strip()

    def __get_blocks(self):
        blocks = []
        file_index_count = []
        file_id = 0
        for i in range(len(self.disk_map)):
            digit = int(self.disk_map[i])
            if i % 2 == 0:
                file_index_count.append((len(blocks), digit))
                blocks.extend([str(file_id)] * digit)
                file_id += 1
            else:
                blocks.extend(["."] * digit)

        return blocks, file_index_count

    def __get_space_count(self, blocks):
        result = []
        i = 0
        while i < len(blocks):
            if blocks[i] == ".":
                start = i
                count = 0
                while i < len(blocks) and blocks[i] == ".":
                    count += 1
                    i += 1
                result.append((start, count))
            else:
                i += 1

        return result

    def part_1(self):
        blocks, _ = self.__get_blocks()
        i, j = 0, len(blocks) - 1
        while i < j:
            while blocks[i] != ".":
                i += 1

            while blocks[j] == ".":
                j -= 1

            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1

        result = 0
        for i in range(len(blocks)):
            if blocks[i] != ".":
                result += i * int(blocks[i])

        return result

    def part_2(self):
        blocks, file_index_count = self.__get_blocks()

        for f in reversed(file_index_count):
            file_index = f[0]
            file_count = f[1]
            space_index_count = self.__get_space_count(blocks[:file_index])
            if len(space_index_count) == 0:
                max_space_count = 0
            else:
                max_space_count = max(space_index_count, key=lambda x: x[1])[1]

            if file_count <= max_space_count:
                i = 0
                while space_index_count[i][0] < file_index:
                    space_index = space_index_count[i][0]
                    space_count = space_index_count[i][1]
                    if file_count <= space_count:
                        (
                            blocks[space_index : (space_index + file_count)],
                            blocks[file_index : (file_index + file_count)],
                        ) = (
                            blocks[file_index : (file_index + file_count)],
                            blocks[space_index : (space_index + file_count)],
                        )
                        break
                    i += 1

        result = 0
        for i in range(len(blocks)):
            if blocks[i] != ".":
                result += i * int(blocks[i])

        return result


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
