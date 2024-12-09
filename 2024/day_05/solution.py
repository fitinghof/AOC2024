from advent import BaseSolution
from collections import defaultdict
from functools import cmp_to_key


class Solution(BaseSolution):
    def part_one(self, input) -> int:
        lines = input.splitlines()
        index = 0
        orderMap = defaultdict(list)
        for index in range(len(lines)):
            if lines[index] == "":
                index += 1
                break
            nums = lines[index].split("|")
            orderMap[nums[1]].append(nums[0])

        sum: int = 0
        readPages: list = []
        for index in range(index, len(lines)):
            pages: list = lines[index].split(",")

            pageValid = True
            for page in pages:
                for req in orderMap[page]:
                    if req in pages and pages.index(req) > pages.index(page):
                        pageValid = False
                        break
                if not pageValid:
                    break
            if pageValid:
                sum += int(pages[int(len(pages) / 2)])

        return sum

    def part_two(self, input) -> int:
        lines = input.splitlines()
        index = 0
        orderMap = defaultdict(list)
        for index in range(len(lines)):
            if lines[index] == "":
                index += 1
                break
            nums = lines[index].split("|")
            orderMap[nums[1]].append(nums[0])

        sum: int = 0
        readPages: list = []
        for index in range(index, len(lines)):
            pages: list = lines[index].split(",")

            pageValid = True
            for pageIndex in range(len(pages)):
                for req in orderMap[pages[pageIndex]]:
                    if req in pages:
                        reqIndex = pages.index(req)
                        if reqIndex > pageIndex:
                            pageValid = False

            if not pageValid:
                def cmp(num1, num2) -> int:
                    if num2 in orderMap[num1]:
                        return -1
                    if num1 in orderMap[num2]:
                        return 1
                    return 0
                pages.sort(key=cmp_to_key(cmp))
                sum += int(pages[int(len(pages) / 2)])

        return sum