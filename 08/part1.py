import re
from common.utils import run_part

instruction_to_index = {
    'L': 0,
    'R': 1,
}


def p1(input: list[str]) -> int:
    instructions = [instruction_to_index[i] for i in input[0]]
    input = input[2:]

    projection = {}
    for line in input:
        src, dest = line.split(' = ')
        projection[src] = tuple(re.findall(r'(\w{3})', dest))

    current_location = 'AAA'
    steps = 0
    while current_location != 'ZZZ':

        current_location = projection[current_location][instructions[steps % len(
            instructions)]]
        steps += 1

    return steps


if __name__ == "__main__":
    run_part("08/input.txt", p1, 1)
