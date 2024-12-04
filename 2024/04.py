from advent import BaseSolution


class Solution(BaseSolution):
    def part_one(self) -> int:
        searchedWords = "XMAS", "SAMX"
        input = self.input.splitlines()
        lineLength = len(input[0])
        sum: int = 0
        for y in range(len(input)):
            for x in range(lineLength):
                word = input[y][x: x + 4]
                if (word in searchedWords):
                    sum += 1
                if y < (len(input) - 3):
                    word = input[y][x] + input[y + 1][x] + input[y + 2][x] + input[y + 3][x]
                    if word in searchedWords:
                        sum += 1
                    if x < (lineLength - 3):
                        word = input[y][x] + input[y + 1][x + 1] + input[y + 2][x + 2] + input[y + 3][x + 3]
                        if word == searchedWords[0] or word == searchedWords[1]:
                            sum += 1
                if x >= 3 and y < (len(input) - 3):
                    word = input[y][x] + input[y + 1][x - 1] + input[y + 2][x - 2] + input[y + 3][x - 3]
                    if word == searchedWords[0] or word == searchedWords[1]:
                            sum += 1

        return sum

    def part_two(self) -> int:
        searchedWords = "MAS", "SAM"
        input = self.input.splitlines()
        lineLength = len(input[0])
        sum: int = 0
        for y in range(1, len(input) - 1):
            for x in range(1, lineLength - 1):
                # wordh = input[y][x - 1 : x + 2]
                # wordv = input[y - 1][x] + input[y][x] + input[y + 1][x]
                # if (wordh in searchedWords) and (wordv in searchedWords):
                #     sum += 1
                wordrd = input[y - 1][x - 1] + input[y][x] + input[y + 1][x + 1]
                wordld = input[y - 1][x + 1] + input[y][x] + input[y + 1][x - 1]
                if (wordrd in searchedWords) and (wordld in searchedWords):
                    sum += 1
        return sum
