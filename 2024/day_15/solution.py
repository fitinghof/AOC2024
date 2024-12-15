from advent import BaseSolution
import enum

def getDir(strDir: str) -> tuple[int, int]:
    match strDir:
        case "^": return (-1, 0)
        case "v": return (1, 0)
        case "<": return (0, -1)
        case ">": return (0, 1)
    return 0, 0
def push(warehouse, pos: tuple[int, int], dir: tuple[int, int], boxShapes = tuple("O")) -> bool:
    y, x = pos
    while warehouse[y][x] in boxShapes:
        y += dir[0]
        x += dir[1]
    if warehouse[y][x] == ".":
        while (y, x) != pos:
            warehouse[y][x] = warehouse[y - dir[0]][x - dir[1]]
            y -= dir[0]
            x -= dir[1]
        return True
    return False

def push2(warehouse, pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    if dir[0] == 0:
        return push(warehouse, pos, dir, ("[", "]"))

    levels: list[set[tuple[int,int]]] = [set()]
    levels[0].add(pos)
    if warehouse[pos[0]][pos[1]] == "[":
        levels[0].add((pos[0], pos[1] + 1))
    else:
        levels[0].add((pos[0], pos[1] - 1))

    level = 0
    while(len(levels) > level):
        for blockPart in levels[level]:
            if warehouse[blockPart[0] + dir[0]][blockPart[1]] in ("[", "]"):
                if len(levels) > level: levels.append(set())
                levels[level + 1].add((blockPart[0] + dir[0], blockPart[1]))
                if warehouse[blockPart[0] + dir[0]][blockPart[1]] == "[":
                    levels[level + 1].add((blockPart[0] + dir[0], blockPart[1] + 1))
                else:
                    levels[level + 1].add((blockPart[0] + dir[0], blockPart[1] - 1))
            elif warehouse[blockPart[0] + dir[0]][blockPart[1]] == "#": return False
        level += 1
    for blocks in reversed(levels):
        for block in blocks:
            warehouse[block[0]][block[1]], warehouse[block[0] + dir[0]][block[1]] = warehouse[block[0] + dir[0]][block[1]], warehouse[block[0]][block[1]]
    return True

class Solution(BaseSolution):
    def __init__(self, input: str, dayPath):
        super().__init__(input, dayPath)
        self.part1_tests([("example_input.txt", 10092),("part1small.txt", 2028)])
        self.part2_tests([("part2small.txt", 618),("example_input.txt", 9021)])
        #("example_input.txt", 9021)

    # The output of parse will be passed as input for part_one and part_two
    def parse(self, input: str):
        parse = input.split("\n\n")
        warehouse: list[list[str]] = [list(i) for i in parse[0].splitlines()]
        path = [i for i in parse[1].replace("\n", "")]
        for i in range(len(warehouse)):
            if "@" in warehouse[i]: return warehouse, path, [i, warehouse[i].index("@")]
        return 0

    def part_one(self, input, rawInput) -> int:
        warehouse, path, robotpos = input
        for strdir in path:
            dir = getDir(strdir)
            canMove = True
            if warehouse[robotpos[0] + dir[0]][robotpos[1] + dir[1]] == "O":
                canMove = push(warehouse, (robotpos[0] + dir[0], robotpos[1] + dir[1]), dir)
            elif warehouse[robotpos[0] + dir[0]][robotpos[1] + dir[1]] == "#":
                canMove = False
            if canMove:
                warehouse[robotpos[0]][robotpos[1]] = "."
                robotpos[0] += dir[0]
                robotpos[1] += dir[1]
                warehouse[robotpos[0]][robotpos[1]] = "@"
        GPSsum = 0
        for y, line in enumerate(warehouse):
            for x, space in enumerate(line):
                if space == "O":
                    GPSsum += y * 100 + x

        return GPSsum

    def part_two(self, input, rawInput: str) -> int:
        some, path, robotpos = input
        warehouse = [list(i.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for i in rawInput.split("\n\n")[0].splitlines()]
        robotpos[1] *= 2
        for ind, strdir in enumerate(path):
            dir = getDir(strdir)
            canMove = True
            if warehouse[robotpos[0] + dir[0]][robotpos[1] + dir[1]] in ("[", "]"):
                canMove = push2(warehouse, (robotpos[0] + dir[0], robotpos[1] + dir[1]), dir)
            elif warehouse[robotpos[0] + dir[0]][robotpos[1] + dir[1]] == "#":
                canMove = False
            if canMove:
                warehouse[robotpos[0]][robotpos[1]] = "."
                robotpos[0] += dir[0]
                robotpos[1] += dir[1]
                warehouse[robotpos[0]][robotpos[1]] = "@"
        GPSsum = 0
        for y, line in enumerate(warehouse):
            for x, space in enumerate(line):
                if space == "[":
                    GPSsum += y * 100 + x

        return GPSsum
