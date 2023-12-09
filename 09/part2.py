from common.utils import run_part
import re


def p2(input: list[str]) -> int:
    return sum([solve_line([int(n) for n in re.findall(r"-?\d+", line)]) for line in input])


def solve_line(sequence: list[int]) -> int:
    end_vals = [sequence[0]]

    w_sequence = sequence.copy()

    while len(set(w_sequence)) != 1:
        w_sequence = [w_sequence[i+1] - v
                      for i, v in enumerate(w_sequence[:-1])]
        end_vals.append(w_sequence[0])

    curr = 0
    for end_val in reversed(end_vals):
        curr = end_val - curr
    return curr


if __name__ == "__main__":
    run_part("09/input.txt", p2, 2)
