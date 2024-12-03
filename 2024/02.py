from advent import BaseSolution

def lineIsSafe(line: str) -> bool:
    num1 = 0
    num2 = 0
    num3 = 0
    for numstr in line.split():
        num1, num2, num3 = num2, num3, num1
        num3 = int(numstr)
        if (num2 == 0):
            continue
        diff = num3 - num2
        if diff == 0 or abs(diff) > 3:
            return False
        if num1 == 0:
            continue
        prevdiff = num2 - num1
        if (diff < 0) != (prevdiff < 0):
            return False
    return True

def lineIsSafe2(line: list[str]) -> bool:
    prevNum = int(line[0])
    decreasing = True
    increasing = True
    for numstr in line[1:]:
        num = int(numstr)
        if (num - prevNum) <= 0 or abs(num - prevNum) > 3:
            increasing = False
            break
        prevNum = num

    prevNum = int(line[0])
    for numstr in line[1:]:
        num = int(numstr)
        if (num - prevNum) >= 0 or abs(num - prevNum) > 3:
            decreasing = False
            break
        prevNum = num

    return decreasing or increasing


class Solution(BaseSolution):
    def part_one(self) -> int:
        safeReports: int = 0
        for line in self.input.splitlines():
            if lineIsSafe(line):
                safeReports += 1
        return safeReports

    def part_two(self) -> int:
        safeReports: int = 0
        for line in self.input.splitlines():
            nums = line.split()
            for i in range(len(nums)):
                if lineIsSafe2(nums[0:i] + nums[i + 1: len(nums)]):
                    safeReports += 1
                    break
        return safeReports
