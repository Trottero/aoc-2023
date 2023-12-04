from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    card_values = []
    for line in input:
        left, winning = line.split(" | ")
        _, card_numbers = left.split(": ")
        winning = [int(x) for x in re.findall(r"\d+", winning)]
        card_numbers = [int(x) for x in re.findall(r"\d+", card_numbers)]

        # count the number of card numbers in winning
        count = 0
        for num in card_numbers:
            if num in winning:
                count += 1

        if count == 0:
            continue

        card_values.append(2 ** (count - 1))

    return sum(card_values)


if __name__ == "__main__":
    run_part("04/input.txt", p1, 1)
