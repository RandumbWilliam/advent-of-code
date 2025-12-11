from collections import Counter

class Advent:
  def __init__(self, input_path):
    self.data = self.__get_data(input_path)
  
  def __get_data(self, input_path):
    left = []
    right = []
    with open(input_path, 'r') as file:
      for line in file:
        left_value, right_value = line.split()

        left.append(int(left_value))
        right.append(int(right_value))

    return (left, right)
  
  def __is_safe(self, report):
    diff = [report[i] - report[i - 1] for i in range(1, len(report))]
    return set(diff) <= {1,2,3} or set(diff) <= {-1,-2,-3}
  
  def part_1(self):
    left, right = self.data
    
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    diff = [abs(l - r) for l,r in zip(left_sorted, right_sorted)]
    return sum(diff)

  def part_2(self):
    left, right = self.data

    right_counter = Counter(right)

    left_sorted = sorted(left)
    right_sorted = sorted(right)

    diff = [l * right_counter.get(l, 0) for l in left]
    return sum(diff)

if __name__ == '__main__':
  advent = Advent("input.txt")
  part_1 = advent.part_1()
  part_2 = advent.part_2()

  print(part_1)
  print(part_2)