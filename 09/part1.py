from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    return sum([solve_line([int(n) for n in re.findall(r"-?\d+", line)]) for line in input])


def solve_line(sequence: list[int]) -> int:
    end_vals = [sequence[-1]]

    w_sequence = sequence.copy()

    while len(set(w_sequence)) != 1:
        w_sequence = [w_sequence[i+1] - v
                      for i, v in enumerate(w_sequence[:-1])]
        end_vals.append(w_sequence[-1])

    return sum(end_vals)


if __name__ == "__main__":
    run_part("09/input.txt", p1, 1)
