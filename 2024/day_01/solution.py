from advent import BaseSolution


class Solution(BaseSolution):
    def part_one(self, input) -> int:
        sum: int = 0
        leftList: list = []
        rightList: list = []
        for line in input.splitlines():
            nums = line.split()
            leftList.append(int(nums[0]))
            rightList.append(int(nums[1]))
        leftList.sort()
        rightList.sort()

        for left, right in zip(leftList, rightList):
            sum += abs(left - right)
        return sum

    def part_two(self, input) -> int:
        sum: int = 0
        leftList: list = []
        rightDict: dict = {}
        for line in input.splitlines():
            nums = line.split()
            left = int(nums[0])
            right = int(nums[1])
            leftList.append(left)
            if right in rightDict:
                rightDict[right] += 1
            else:
                rightDict[right] = 1
        for num in leftList:
            if num in rightDict:
                sum += num * rightDict[num]
        return sum

