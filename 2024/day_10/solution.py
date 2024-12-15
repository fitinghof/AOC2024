from advent import BaseSolution

def evaluate_trailhead(list: list[list[int]], y: int, x: int, black_list: set | None, step: int = 0):
    if y not in range(len(list)) or x not in range(len(list[0])) or list[y][x] != step: return 0
    if step == 9:
        if black_list is None:
            return 1
        elif (y, x) not in black_list:
            black_list.add((y, x))
            return 1
        else : return 0
    return sum(evaluate_trailhead(list, y, x, black_list, step + 1) for y, x in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)])

class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([("example_input.txt", 36)])
        self.part2_tests([("example_input.txt", 81)])

    def parse(self, input: str):
        return [[int(e) for e in row] for row in input.splitlines()]

    def part_one(self, input, rawInput) -> int:
        return sum(evaluate_trailhead(input, y, x, set()) for x in range(len(input[0])) for y in range(len(input)))

    def part_two(self, input, rawInput) -> int:
        return sum(evaluate_trailhead(input, y, x, None) for x in range(len(input[0])) for y in range(len(input)))
