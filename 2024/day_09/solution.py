from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input) -> list[int]:
        disk: list = []
        free = False
        id = 0
        for c in input:
            for i in range(int(c)):
                if not free:
                    disk.append(id)
                else: disk.append(None)
            id += not free
            free = not free
        return disk

    part1_ex_answer = 1928
    def part_one(self, input) -> int:
        disk: list = input

        firstFree = disk.index(None)
        lastIndex = len(disk) - 1

        while(firstFree < lastIndex):
            disk[firstFree], disk[lastIndex] = disk[lastIndex], disk[firstFree]
            while(disk[lastIndex] is None and lastIndex > firstFree):
                lastIndex -= 1
            while(disk[firstFree] is not None and lastIndex > firstFree):
                firstFree += 1
        sum = 0
        for i, id in enumerate(disk):
            if id is None: break
            sum += id * i

        return sum

    part2_ex_answer = 2858
    def part_two(self, input) -> int:
        disk: list = input

        fileIndex = len(disk) - 1
        freeIndex = disk.index(None)
        while(freeIndex < fileIndex):
            id = disk[fileIndex]

            fileLen = 1
            while(disk[fileIndex - 1] == id):
                fileLen += 1
                fileIndex -= 1

            while(freeIndex < fileIndex):

                freeLen = 0
                while(disk[freeIndex + freeLen] is None):
                    freeLen += 1

                if freeLen >= fileLen:
                    for i in range(fileLen):
                        disk[freeIndex + i] = id
                        disk[fileIndex + i] = None
                    break
                else:
                    freeIndex += freeLen
                    while(disk[freeIndex] is not None):
                        freeIndex += 1
            fileIndex -= 1
            while(disk[fileIndex] is None):
                fileIndex -= 1
            freeIndex = disk.index(None)

        sum = 0
        for i, c in enumerate(disk):
            if c is not None:
                sum += int(c) * i

        return sum