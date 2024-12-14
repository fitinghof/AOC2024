from advent import BaseSolution
import re
import math
import time

def possibleChristmasTree(bathroom: list[list[str]]) -> bool:
    longLines = 0
    for line in bathroom:
        if line.count("#") > 30: longLines += 1
        if longLines == 2: return True
    return False

class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([("example_input.txt", 21)])
        self.part2_tests([])

    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        return  [[int(j) for j in i] for i in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", input)]

    def part_one(self, input) -> int:
        WIDTH = 101
        HEIGHT = 103
        ITERATIONS = 100
        quads = [[0,0],[0,0]]
        for robot in input:
            robot[0] = (robot[0] + robot[2] * ITERATIONS) % WIDTH
            robot[1] = (robot[1] + robot[3] * ITERATIONS) % HEIGHT
            if robot[0] != (WIDTH // 2) and robot[1] != (HEIGHT // 2):
                quads[robot[0] > (WIDTH // 2)][robot[1] > (HEIGHT // 2)] += 1
        return quads[0][0] * quads[0][1] * quads[1][0] * quads[1][1]

    def part_two(self, input) -> int:
        WIDTH = 101
        HEIGHT = 103
        for j in range(WIDTH * HEIGHT):
            newBoard: list[list[str]] = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
            for robot in input:
                robot[0] = (robot[0] + robot[2]) % WIDTH
                robot[1] = (robot[1] + robot[3]) % HEIGHT
                newBoard[robot[1]][robot[0]] = "#"
            if possibleChristmasTree(newBoard):
                print(j + 1)
                for i in newBoard: print("".join(i))

        quads = [[0,0],[0,0]]
        for robot in input:
            if robot[0] == (WIDTH // 2) or robot[1] == (HEIGHT // 2): continue

            quads[robot[0] > (WIDTH // 2)][robot[1] > (HEIGHT // 2)] += 1
        return quads[0][0] * quads[0][1] * quads[1][0] * quads[1][1]
