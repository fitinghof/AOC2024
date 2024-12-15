from advent import BaseSolution
import re
import math

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def solve_linear_diophantine(a, b, c):
    gcd, x0, y0 = extended_euclidean(a, b)
    if c % gcd != 0:
        return None  # No solution
    x0 *= c // gcd
    y0 *= c // gcd
    return x0, y0, gcd

class Solution(BaseSolution):
    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        output: list = []
        for game in input.split("\n\n"):
            gameOut: list = []
            for line in game.splitlines():
                gameOut.append([int(i) for i in re.findall(r'\d+', line)])
            output.append(gameOut)
        return output

    part1_ex_answer = 480
    def part_one(self, input, rawInput) -> int:
        for game in input:
            x = game[0][0] + game[1][0]
            y = game[0][1] + game[1][1]
            goal = game[2][0] + game[2][1]
            gcdxy = math.gcd(x, y)
            if goal % gcdxy == 0:
                print(solve_linear_diophantine(game[0][0], game[1][0], game[2][0]))
        return 0

    part2_ex_answer = 0
    def part_two(self, input, rawInput) -> int:
        return 0
