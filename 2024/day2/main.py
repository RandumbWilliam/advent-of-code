class Advent:
  def __init__(self, input_path):
    self.data = self.__get_data(input_path)
  
  def __get_data(self, input_path):
    with open(input_path, 'r') as file:
      lines = file.readlines()

    return [list(map(int, line.split())) for line in lines]
  
  def __is_safe(self, report):
    diff = [report[i] - report[i - 1] for i in range(1, len(report))]
    return set(diff) <= {1,2,3} or set(diff) <= {-1,-2,-3}
  
  def part_1(self):
    safe = 0
    for report in self.data:
      if self.__is_safe(report):
        safe += 1
    
    return safe

  def part_2(self):
    safe = 0
    for report in self.data:
      if self.__is_safe(report):
        safe += 1
      else:
        for i in range(len(report)):
          if self.__is_safe(report[:i] + report[i+1:]):
            safe += 1
            break
    
    return safe

if __name__ == '__main__':
  advent = Advent("input.txt")
  part_1 = advent.part_1()
  part_2 = advent.part_2()

  print(part_1)
  print(part_2)