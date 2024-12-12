from advent import BaseSolution
from collections import defaultdict

def solve(input: defaultdict, blinks):
    for _ in range(blinks):
        newInput: defaultdict = defaultdict(int)
        for key, value in input.items():
            if key == 0:
                newInput[1] += value
            else:
                digitLen = len(str(key))
                if digitLen % 2 == 0:
                    newInput[int(str(key)[:digitLen//2])] += value
                    newInput[int(str(key)[digitLen//2:])] += value
                else:
                    newInput[key * 2024] += value
        input = newInput
    return sum(input.values())

class Solution(BaseSolution):
    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        stones: defaultdict = defaultdict(int)
        for i in input.split(): stones[int(i)] += 1
        return stones

    part1_ex_answer = 55312
    def part_one(self, input) -> int:
        return solve(input, 25)

    part2_ex_answer = 65601038650482
    def part_two(self, input) -> int:
        return solve(input, 75)
