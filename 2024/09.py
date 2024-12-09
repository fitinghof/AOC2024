from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self) -> list[int]:
        disk: list = []
        free = False
        id = 0
        for c in self.input:
            for i in range(int(c)):
                if not free:
                    disk.append(id)
                else: disk.append(None)
            id += not free
            free = not free
        return disk

    def part_one(self) -> int:
        disk: list = self.parse()

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

    def part_two(self) -> int:
        disk: list = self.parse()

        lastIndex = len(disk) - 1
        firstFree = disk.index(None)
        while(firstFree < lastIndex):
            id = disk[lastIndex]

            lastLen = 0
            while(disk[lastIndex - lastLen] == id):
                lastLen += 1

            while(firstFree < lastIndex):

                freeLen = 0
                while(disk[firstFree + freeLen] is None):
                    freeLen += 1

                if freeLen >= lastLen:
                    for i in range(lastLen):
                        disk[firstFree + i] = id
                        disk[lastIndex - i] = None
                    break
                else:
                    firstFree += freeLen
                    while(disk[firstFree] is not None):
                        firstFree += 1
            lastIndex -= lastLen
            while(disk[lastIndex] is None):
                lastIndex -= 1
            firstFree = disk.index(None)

        sum = 0
        for i, c in enumerate(disk):
            if c is not None:
                sum += int(c) * i

        return sum