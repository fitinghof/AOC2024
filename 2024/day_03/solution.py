from advent import BaseSolution


class Solution(BaseSolution):
    def part_one(self, input, rawInput) -> int:
        result: int = 0
        mulIndex: int = 0
        while mulIndex < len(input):
            mulIndex = input.find("mul(", mulIndex)
            if mulIndex == -1: return result
            numstr: str = ""
            mulIndex += 4
            num1: int = 0
            num2: int = 0
            while mulIndex < len(input) and input[mulIndex].isdigit():
                numstr += input[mulIndex]
                mulIndex += 1
            if numstr != "":
                num1 = int(numstr)
                numstr = ""
                if input[mulIndex] == ",":
                    mulIndex += 1
                    while mulIndex < len(input) and input[mulIndex].isdigit():
                        numstr += input[mulIndex]
                        mulIndex += 1
                    if numstr != "":
                        num2 = int(numstr)
                        if input[mulIndex] == ")":
                            result += num1 * num2
        return result




    def part_two(self, input, rawInput) -> int:
        result: int = 0
        mulIndex: int = 0
        do: bool = True
        doordontIndex = 0
        lastDoorDont = 0
        while mulIndex < len(input):
            mulIndex = input.find("mul(", mulIndex)
            dontIndex = input.rfind("don't()", 0, mulIndex)
            doIndex = input.rfind("do()", 0, mulIndex)

            if not (doIndex == -1 and dontIndex == -1):
                if doIndex == -1 and dontIndex != -1:
                    do = False
                elif dontIndex == -1 and doIndex != -1:
                    do = True
                else: do = doIndex > dontIndex

            if mulIndex == -1: return result
            numstr: str = ""
            mulIndex += 4
            num1: int = 0
            num2: int = 0
            while mulIndex < len(input) and input[mulIndex].isdigit():
                numstr += input[mulIndex]
                mulIndex += 1
            if numstr != "":
                num1 = int(numstr)
                numstr = ""
                if input[mulIndex] == ",":
                    mulIndex += 1
                    while mulIndex < len(input) and input[mulIndex].isdigit():
                        numstr += input[mulIndex]
                        mulIndex += 1
                    if numstr != "":
                        num2 = int(numstr)
                        if input[mulIndex] == ")":
                            if do:
                                result += num1 * num2
        return result
