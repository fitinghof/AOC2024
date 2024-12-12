from advent import BaseSolution
from collections import defaultdict


class Solution(BaseSolution):
    def parse(self, input: str):
        #return [list(i) for i in input.splitlines()]
        towers = defaultdict(list)
        lines = [list(i) for i in input.splitlines()]
        height = len(lines)
        width = len(lines[0])
        for y in range(height):
            for x in range(width):
                if lines[y][x] != ".":
                    towers[lines[y][x]].append((y,x))
        return towers, lines, height, width

    part1_ex_answer = 14

    def part_one(self, input) -> int:
        towers, lines, height, width = input
        sum = 0
        for freq in towers.values():
            for i in range(len(freq)):
                for j in range(i + 1,len(freq)):
                    xofset = freq[j][1] - freq[i][1]
                    yofset = freq[j][0] - freq[i][0]

                    ypos = freq[i][0] - yofset
                    xpos = freq[i][1] - xofset

                    coveredPos = []
                    if ypos in range(height) and xpos in range(width):
                        if lines[ypos][xpos] == "." and (ypos, xpos) not in coveredPos:
                            coveredPos.append((ypos, xpos))
                            sum += 1

                    ypos = freq[j][0] + yofset
                    xpos = freq[j][1] + xofset
                    if ypos in range(height) and xpos in range(width):
                        if lines[ypos][xpos] == "." and (ypos, xpos) not in coveredPos:
                            coveredPos.append((ypos, xpos))
                            sum += 1
        return sum

    part2_ex_answer = 34

    def part_two(self, input) -> int:
        towers, lines, height, width = input
        for freq in towers.values():
            for i in range(len(freq)):
                for j in range(i + 1,len(freq)):
                    xofset = freq[j][1] - freq[i][1]
                    yofset = freq[j][0] - freq[i][0]

                    ypos = freq[i][0]
                    xpos = freq[i][1]

                    while xpos in range(width) and ypos in range(height):
                        lines[ypos][xpos] = "#"
                        xpos += xofset
                        ypos += yofset

                    ypos = freq[j][0]
                    xpos = freq[j][1]
                    while xpos in range(width) and ypos in range(height):
                        lines[ypos][xpos] = "#"
                        xpos -= xofset
                        ypos -= yofset

        return sum([i.count("#") for i in lines])

