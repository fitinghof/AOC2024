from advent import BaseSolution
from collections import defaultdict


class Solution(BaseSolution):
    def parse(self):
        return [list(i) for i in self.input.splitlines()]

    def part_one(self) -> int:
        towers = defaultdict(list)
        lines = self.parse()
        height = len(lines)
        sum = 0
        width = len(lines[0])
        for y in range(height):
            for x in range(width):
                if lines[y][x] != ".":
                    towers[lines[y][x]].append((y,x))
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

    def part_two(self) -> int:
        towers = defaultdict(list)
        lines = self.parse()
        height = len(lines)
        sum = 0
        width = len(lines[0])
        for y in range(height):
            for x in range(width):
                if lines[y][x] != ".":
                    towers[lines[y][x]].append((y,x))
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
        for i in lines: sum += i.count("#")
        return sum
