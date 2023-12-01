from common.utils import run_part
import re

words_to_values = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def p2(input: list[str]) -> int:
    digits = []
    for line in input:
        numbers = [words_to_values[x.group(1)] for x in re.finditer(
            "(?=(\d|"+"|".join(words_to_values.keys()) + "))", line)]

        digits.append(int(f'{numbers[0]}{numbers[-1]}'))

    return sum(digits)


if __name__ == "__main__":
    run_part("01/input.txt", p2, 2)
