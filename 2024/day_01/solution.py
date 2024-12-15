from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str):
        outPut = []
        for i in input.splitlines():
            outPut.append([int(j) for j in i.split()])
        return outPut

    def part_one(self, input, rawInput) -> int:
        leftList: list = []
        rightList: list = []
        for line in input:
            leftList.append(line[0])
            rightList.append(line[1])
        leftList.sort()
        rightList.sort()

        return sum(abs(left - right) for left, right in zip(leftList, rightList))

    def part_two(self, input, rawInput) -> int:
        sum: int = 0
        leftList: list = []
        rightDict: dict = {}
        for line in input:
            left = line[0]
            right = line[1]
            leftList.append(left)
            if right in rightDict:
                rightDict[right] += 1
            else:
                rightDict[right] = 1
        for num in leftList:
            if num in rightDict:
                sum += num * rightDict[num]
        return sum

