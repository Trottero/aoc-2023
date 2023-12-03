import re
from common.utils import run_part


def p2(input: list[str]) -> int:
    # Numbers are stored in a tuple, (value, line, xstart, xend, validity)
    numbers = []
    for i, line in enumerate(input):
        numbers.extend([(m.group(), i, m.start(), m.end() - 1, False)
                       for m in re.finditer(r"\d+", line)])

    symbols = []
    for i, line in enumerate(input):
        # Find the symbols on this line
        for si, s in enumerate(line):
            if s == "*":
                symbols.append((s, i, si))

    # Check if any number has a valid symbol on the same line or around it
    valid_parts = []

    for i, (value, line, xstart, xend, validity) in enumerate(numbers):
        for si, (symbol, sline, sx) in enumerate(symbols):
            if abs(sline - line) <= 1 and sx >= xstart - 1 and sx <= xend + 1:
                valid_parts.append((value, si))

    valid_parts = sorted(valid_parts, key=lambda x: x[1])

    # Remove distinct parts
    valid_parts = list(filter(lambda x: len(list(
        filter(lambda y: y[1] == x[1], valid_parts))) == 2, valid_parts))

    gear_ratios = []
    # Mulitply parts that share the same symbol
    for i in range(0, len(valid_parts), 2):
        gear_ratios.append(int(valid_parts[i][0]) *
                           int(valid_parts[i + 1][0]))

    return sum(gear_ratios)


if __name__ == "__main__":
    run_part("03/input.txt", p2, 2)
