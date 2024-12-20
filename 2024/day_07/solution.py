from advent import BaseSolution

def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def cat(num1: int, num2: int):
    return int(str(num1) + str(num2))

def has_solution(list, operations, operation = add, sum = 0, startIndex = 1):
    if startIndex == len(list): return sum
    sum = operation(sum, list[startIndex])
    if sum > list[0]: return sum
    for op in operations:
        if has_solution(list, operations, op, sum, startIndex + 1) == list[0]:
            return list[0]
    return 0

class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([("example_input.txt", 3749)])
        self.part2_tests([("example_input.txt", 11387)])

    def parse(self, input):
        data = []
        for line in input.splitlines():
            parsedLine = line.split()
            parsedLine[0] = parsedLine[0].removesuffix(":")
            data.append([int(i) for i in parsedLine])
        return data

    def part_one(self, input, rawInput) -> int:
        return sum(has_solution(line, [add, mul]) for line in input)

    def part_two(self, input, rawInput) -> int:
        return sum(has_solution(line, [add, mul, cat]) for line in input)