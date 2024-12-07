from advent import BaseSolution

class Solution(BaseSolution):
    def parse(self):
        data = []
        for line in self.input.splitlines():
            parsedLine = line.split()
            parsedLine[0] = parsedLine[0].removesuffix(":")
            data.append([int(i) for i in parsedLine])
        return data


    def part_one(self) -> int:
        lines = self.parse()
        totalSum: int = 0
        for line in lines:
            for i in range(1 << (len(line) - 1)):
                sum: int = line[1]
                for sign in range(2, len(line)):
                    if (i & (1 << (sign - 2))):
                        sum += line[sign]
                    else: sum *= line[sign]
                if sum == line[0]:
                    totalSum += line[0]
                    break
        return totalSum

    def part_two(self) -> int:
        lines = self.parse()
        totalSum: int = 0
        for lineNum, line in enumerate(lines):
            for wack in range(1 << (len(line) - 1)):
                foundSolution = False
                for i in range(1 << (len(line) - 1)):
                    sum: int = line[1]
                    #testLine = str(sum)
                    for sign in range(2, len(line)):
                        if wack & (1 << (sign - 2)):
                            sum = int(str(sum) + str(line[sign]))
                            #testLine += " || " + str(line[sign])
                        elif (i & (1 << (sign - 2))):
                            sum *= line[sign]
                            #testLine += " * " + str(line[sign])
                        else: 
                            sum += line[sign]
                            #testLine += " + " + str(line[sign])
                        if sum > line[0]: break
                    if sum == line[0]:
                        #print(lineNum)
                        #print(line[0], "=" , testLine)
                        totalSum += line[0]
                        foundSolution = True
                        break
                if foundSolution:
                    break
        return totalSum