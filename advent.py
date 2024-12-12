from argparse import ArgumentParser
from datetime import date
from importlib import import_module
from types import ModuleType
from typing import Callable, Optional
from pathlib import Path


class BaseSolution:
    input: str
    example_input: str
    part1_ex_answer: int = 0
    part2_ex_answer: int = 0
    def __init__(self, input: str, example_input: str):
        self.input = input
        self.example_input = example_input

    def parse(self, input):
        return input

    def part_one(self, input) -> int:
        raise NotImplementedError("Part one yet to be implemented")

    def part_two(self, input) -> int:
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
    example_input: str = ""

    try:
        with open(input_path, "r") as f:
            input = f.read()
        with open(example_input_path, "r") as f:
            example_input = f.read()
    except FileNotFoundError:
        print(f"[ERR] Could not open puzzle input [{input_path} or {example_input_path} or both]")

    if len(example_input) == 0:
        print("WARNING No example input")
    if len(input) == 0:
        print("WARNING No input")

    solution: BaseSolution = module.Solution(input, example_input)

    ex_answer = solution.part_one(solution.parse(example_input))
    if solution.part1_ex_answer == ex_answer or len(example_input) == 0:
        print("Part 1:", solution.part_one(solution.parse(input)))
    else:
        print(f"Part 1: Failed to get correct output using example input, you got {ex_answer}, correct: {solution.part1_ex_answer}")

    ex_answer = solution.part_two(solution.parse(example_input))
    if solution.part2_ex_answer == ex_answer or len(example_input) == 0:
        print("Part 2:", solution.part_two(solution.parse(input)))
    else:
        print(f"Part 2: Failed to get correct output using example input, you got {ex_answer}, correct: {solution.part2_ex_answer}")

if __name__ == "__main__":
    main()
