from advent import BaseSolution
from collections import defaultdict
from itertools import chain

def floodFill(input: list[list[str]], y: int, x: int, type, altered: list[list[str]]):
    if y not in range(len(input)) or x not in range(len(input[0])) or input[y][x] != type:
        return 0, 1
    if altered[y][x] == type: return 0, 0
    altered[y][x] = type
    flowers = 1
    fences = 0
    for y, x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        tmpflowers, tmpfences = floodFill(input, y, x, type, altered)
        flowers += tmpflowers
        fences += tmpfences
    return flowers, fences

def floodFill2(input: list[list[str]], y: int, x: int, type, altered: list[list], yfences, xfences):
    if altered[y][x] != None: return 0
    altered[y][x] = type
    flowers = 1
    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if y2 not in range(len(input)) or x2 not in range(len(input[0])) or type != input[y2][x2]:
            if x != x2:
                yfences[(x, x > x2)].append(y)
            else:
                xfences[(y, y > y2)].append(x)
        else:
            flowers += floodFill2(input, y2, x2, type, altered, yfences, xfences)
    return flowers

def counter(input, y, x, altered):
    yfences = defaultdict(list)
    xfences = defaultdict(list)
    flowers = floodFill2(input, y, x, input[y][x], altered, yfences, xfences)
    fences = 0
    for fenceRow in chain(yfences.values(), xfences.values()):
        fenceRow.sort()
        for i in range(1,len(fenceRow)):
            if (fenceRow[i - 1] + 1) != fenceRow[i]:
                fences += 1
        fences += 1
    return flowers, fences


class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([])
        self.part2_tests([])
    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        return [[str(i) for i in j] for j in input.splitlines()]

    def part_one(self, input) -> int:
        totalPlotValue = 0
        altered: list = [[None for _ in range(len(i))] for i in input]
        for y in range(len(input)):
            for x in range(len(input[0])):
                if altered[y][x] is None:
                    flowers, fences = floodFill(input, y, x, input[y][x], altered)
                    totalPlotValue += flowers * fences
        return totalPlotValue

    def part_two(self, input) -> int:
        totalPlotValue = 0
        altered: list = [[None for _ in range(len(i))] for i in input]
        for y in range(len(input)):
            for x in range(len(input[0])):
                if altered[y][x] is None:
                    flowers, fences = counter(input, y, x, altered)
                    totalPlotValue += flowers * fences
        return totalPlotValue
