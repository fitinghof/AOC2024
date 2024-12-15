from argparse import ArgumentParser
from datetime import date
from importlib import import_module
from types import ModuleType
from typing import Callable, Optional
from pathlib import Path

class BaseSolution:
    input: str
    dayPath: Path
    part1_test: list[tuple[str, int]] = []
    part2_test: list[tuple[str, int]] = []

    def __init__(self, input: str, dayPath):
        self.dayPath = dayPath
        self.input = input

    def parse(self, input):
        return input

    def part1_tests(self, tests: list[tuple[str, int]]):
        self.part1_test = tests[:]

    def part2_tests(self, tests: list[tuple[str, int]]):
        self.part2_test = tests[:]

    def test(self, func, tests):
        success = True
        for test in tests:
            try:
                f = open(self.dayPath / test[0], "r")
            except:
                print(f"---WARNING--- failed to run test: {test[0]}")
            else:
                input = f.read()
                f.close()
                success = True
                if len(input) == 0: print(f"---WARNING--- test: {test[0]} has no data")
                if (answer := func(self.parse(input), input)) != test[1]:
                    print(f"test {test[0]} failed, got: {answer}, expected: {test[1]}")
                    success = False
        return success

    def part_one(self, input, rawInput) -> int:
        raise NotImplementedError("Part one yet to be implemented")

    def part_two(self, input, rawInput) -> int:
        raise NotImplementedError("Part two yet to be implemented")


def get_parser() -> ArgumentParser:
    parser = ArgumentParser("advent")

    today = date.today()
    parser.add_argument("-y", "--year", type=int, default=today.year)
    parser.add_argument("-d", "--day", type=int, default=today.day)

    return parser

def main():
    args = get_parser().parse_args()

    assert args.day in range(1, 26)

    year: int = args.year
    day: int = args.day
    year_path = Path(".", str(year))
    day_path = Path(year_path, f"day_{day:02}")

    solution_path = day_path / "solution.py"
    input_path = day_path / "input.txt"
    example_input_path = day_path / "example_input.txt"

    if not day_path.exists():
        day_path.mkdir(parents=True, exist_ok=True)

    if not solution_path.exists():
        with open(solution_path, "x") as f, open("./template.py", "r") as g:
            f.write(g.read())
    if not example_input_path.exists():
        with open(example_input_path, "x") as f:
            pass
    if not input_path.exists():
        with open(input_path, "x") as f:
            pass

    module_name = f"{year}.day_{day:02}.solution"

    module: ModuleType = import_module(module_name)
    input: str = ""


    try:
        with open(input_path, "r") as f:
            input = f.read()
    except FileNotFoundError:
        print(f"[ERR] Could not open puzzle input [{input_path} or {example_input_path} or both]")
    if len(input) == 0:
        print("WARNING No input")

    solution: BaseSolution = module.Solution(input, day_path)

    if solution.test(solution.part_one, solution.part1_test):
        print(f"Part 1: {solution.part_one(solution.parse(input), input)}")
    if solution.test(solution.part_two, solution.part2_test):
        print(f"Part 2: {solution.part_two(solution.parse(input), input)}")



if __name__ == "__main__":
    main()
