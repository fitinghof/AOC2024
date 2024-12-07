from advent import BaseSolution

def has_loop(map, startpos):
    mapHeight = len(map)
    mapWidth = len(map[0])
    pos = startpos
    map[pos[0]][pos[1]] = "X"
    dirIndex = 0
    dirs = (-1, 0), (0, 1), (1, 0), (0, -1)
    map[pos[0]][pos[1]] = dirIndex
    while (pos[0] + dirs[dirIndex][0]) in range(mapHeight) and (pos[1] + dirs[dirIndex][1]) in range(mapWidth):
        if map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] != "#":
            if map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] == str(dirIndex):
                return True
            map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] = str(dirIndex)
            pos[0] += dirs[dirIndex][0]
            pos[1] += dirs[dirIndex][1]
        else: dirIndex = (dirIndex + 1) % 4
    return False

class Solution(BaseSolution):
    def part_one(self) -> int:
        map = [list(i) for i in self.input.splitlines()]
        pos = [0, 0]
        mapHeight = len(map)
        mapWidth = len(map[0])
        for i in range(mapHeight):
            if "^" in map[i]:
                pos = [i, map[i].index("^")]
                break
        map[pos[0]][pos[1]] = "X"
        dirIndex = 0
        dirs = (-1, 0), (0, 1), (1, 0), (0, -1)
        while (pos[0] + dirs[dirIndex][0]) in range(mapHeight) and (pos[1] + dirs[dirIndex][1]) in range(mapWidth):
            if map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] != "#":
                map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] = "X"
                pos[0] += dirs[dirIndex][0]
                pos[1] += dirs[dirIndex][1]
            else: dirIndex = (dirIndex + 1) % 4
        sum = 0
        for line in map:
            sum += line.count("X")
        return sum

    def part_two(self) -> int:
        map = [list(i) for i in self.input.splitlines()]
        startpos = [0, 0]
        mapHeight = len(map)
        mapWidth = len(map[0])
        for i in range(mapHeight):
            if "^" in map[i]:
                startpos = [i, map[i].index("^")]
                break
        
        
        pos = startpos.copy()
        dirIndex = 0
        dirs = (-1, 0), (0, 1), (1, 0), (0, -1)
        sum = 0
        while (pos[0] + dirs[dirIndex][0]) in range(mapHeight) and (pos[1] + dirs[dirIndex][1]) in range(mapWidth):
            if map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] != "#":
                if map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] != "X":
                    map[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] = "X"
                    mapCopy = [i[:] for i in map]
                    mapCopy[pos[0] + dirs[dirIndex][0]][pos[1] + dirs[dirIndex][1]] = "#"
                    if has_loop(mapCopy, startpos.copy()):
                        sum += 1
                pos[0] += dirs[dirIndex][0]
                pos[1] += dirs[dirIndex][1]
            else: dirIndex = (dirIndex + 1) % 4
        return sum
