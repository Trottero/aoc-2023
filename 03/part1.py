import re
from common.utils import run_part


def p1(input: list[str]) -> int:
    # Numbers are stored in a tuple, (value, line, xstart, xend, validity)
    numbers = []
    for i, line in enumerate(input):
        numbers.extend([(m.group(), i, m.start(), m.end() - 1, False)
                       for m in re.finditer(r"\d+", line)])

    symbols = []
    for i, line in enumerate(input):
        # Find the symbols on this line
        for si, s in enumerate(line):
            if not s.isdigit() and s != ".":
                symbols.append((s, i, si))

    # Check if any number has a valid symbol on the same line or around it
    for i, (value, line, xstart, xend, validity) in enumerate(numbers):
        for symbol, sline, sx in symbols:
            if abs(sline - line) <= 1 and sx >= xstart - 1 and sx <= xend + 1:
                numbers[i] = (value, line, xstart, xend, True)

    return sum(int(value) for value, _, _, _, validity in numbers if validity)


if __name__ == "__main__":
    run_part("03/input.txt", p1, 1)
