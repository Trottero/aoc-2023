from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    vals = []
    for line in input:
        row, groups = line.split(" ")
        groups = [int(x) for x in groups.split(",")]
        tests = ['']
        for c in row:
            if c != "?":
                tests = [test + c for test in tests]
            else:
                tests = [test + "#" for test in tests] + \
                    [test + "." for test in tests]

        regex = f"^[.]*{'[.]+'.join(['#'*x for x in groups])}[.]*$"
        vals.append(
            sum([1 for test in tests if re.search(regex, test) is not None]))
    return sum(vals)


if __name__ == "__main__":
    run_part("12/input.txt", p1, 1)
