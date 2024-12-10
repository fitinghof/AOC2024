from advent import BaseSolution

def evaluate_trailhead(list, y, x, black_list: set | None, step = 0):
    if list[y][x] != step: return 0
    if step == 9:
        if black_list is None:
            return 1
        elif (y, x) not in black_list:
            black_list.add((y, x))
            return 1
        else : return 0
    sum = 0
    for y, x in [(y  -1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if y in range(len(list)) and x in range(len(list[0])):
            sum += evaluate_trailhead(list, y, x, black_list, step + 1)
    return sum


class Solution(BaseSolution):
    def parse(self, input: str):
        map: list = []
        for i in input.splitlines():
            map.append([int(j) for j in i])
        return map

    def part1_ex_answer(self) -> int:
        return 36

    def part_one(self, input) -> int:
        return sum(evaluate_trailhead(input, y, x, set()) for x in range(len(input[0])) for y in range(len(input)))

    def part2_ex_answer(self) -> int:
        return 81

    def part_two(self, input) -> int:
        return sum(evaluate_trailhead(input, y, x, None) for x in range(len(input[0])) for y in range(len(input)))
