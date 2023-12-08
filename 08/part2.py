import math
import re
from common.utils import run_part

instruction_to_index = {
    'L': 0,
    'R': 1,
}

projection = {}


def p2(input: list[str]) -> int:
    instructions = [instruction_to_index[i] for i in input[0]]
    input = input[2:]

    for line in input:
        src, dest = line.split(' = ')
        projection[src] = tuple(re.findall(r'(\w{3})', dest))

    starting_locations = [k for k in projection.keys() if k.endswith('A')]

    path_completion_steps = [solve_for_path(
        starting_location, instructions) for starting_location in starting_locations]

    return math.lcm(*path_completion_steps)


def solve_for_path(starting_location: str, instructions: list[int]) -> int:
    current_location = starting_location
    steps = 0
    while not current_location.endswith('Z'):

        current_location = projection[current_location][instructions[steps % len(
            instructions)]]
        steps += 1

    return steps


if __name__ == "__main__":
    run_part("08/input.txt", p2, 2)
