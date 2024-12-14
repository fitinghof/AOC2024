from advent import BaseSolution


class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([("example_input.txt", 0)])
        self.part2_tests([("example_input.txt", 0)])

    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        return input

    def part_one(self, input) -> int:
        return 0

    def part_two(self, input) -> int:
        return 0
