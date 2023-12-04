import re
from common.utils import run_part


def p2(input: list[str]) -> int:
    card_values = {}
    for line in input:
        left, winning = line.split(" | ")
        card_id, card_numbers = left.split(": ")
        winning = [int(x) for x in re.findall(r"\d+", winning)]
        card_numbers = [int(x) for x in re.findall(r"\d+", card_numbers)]
        card_id = int(re.search(r"\d+", card_id).group())

        # count the number of card numbers in winning
        count = 0
        for num in card_numbers:
            if num in winning:
                count += 1

        # Record that this card wins x amount of cards
        card_values[card_id] = [x for x in range(
            card_id + 1, card_id + count + 1)]

    card_inventory = {card_id: 1 for card_id in card_values.keys()}

    # Iterate through it once adding up the total number of cards each card wins
    for card_id, card_wins in card_values.items():
        for card_win in card_wins:
            card_inventory[card_win] += card_inventory[card_id]

    return sum(card_inventory.values())


if __name__ == "__main__":
    run_part("04/input.txt", p2, 2)
