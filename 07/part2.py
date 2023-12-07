from functools import cmp_to_key
from common.utils import run_part


input_to_value = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def p2(input: list[str]) -> int:
    valued_cards = []

    for line in input:
        cards, bet = line.split(" ")
        valued_cards.append((convert_to_value(cards), int(bet)))

    sorted_cards = sorted(
        valued_cards, key=cmp_to_key(compare_hands))

    summed = 0
    for i, (_, bet) in enumerate(sorted_cards):
        summed += bet * (i + 1)

    return summed


rules = {
    'five_of_a_kind': lambda hand: len(set(hand)) == 1 or any(hand.count(card) == 5 - hand.count(0) for card in hand if card != 0),
    'four_of_a_kind': lambda hand: hand.count(0) == 4 or any(hand.count(card) == 4 - hand.count(0) for card in hand if card != 0),
    'full_house': lambda hand: any(hand.count(card) == 3 - hand.count(0) and any(hand.count(innercard) == 2 - (min(hand.count(0) - 3 + hand.count(card), hand.count(0))) for innercard in hand if innercard != card and innercard != 0) for card in hand if card != 0),
    'three_of_a_kind': lambda hand: hand.count(0) == 3 or any(hand.count(card) == 3 - hand.count(0) for card in hand if card != 0),
    'two_pairs': lambda hand: any(hand.count(card) == 2 - hand.count(0) for card in hand if card != 0) and len(set(hand)) == 3 - min(1, hand.count(0)),
    'one_pair': lambda hand: any(hand.count(card) == 2 - hand.count(0) for card in hand if card != 0),
    'high_card': lambda hand: True,
}


def get_hand_value(hand: tuple[int, int, int, int, int]) -> int:
    for i, rule in enumerate(rules.values()):
        if rule(hand):
            return len(rules) - i


def compare_hands(x: tuple[tuple[int, int, int, int, int], int], y: tuple[tuple[int, int, int, int, int], int]) -> int:
    # Positive if x wins, negative if y wins, 0 if tie
    left = get_hand_value(x[0])
    right = get_hand_value(y[0])
    if left == right:
        # Tie, compare cards
        for i, v in enumerate(x[0]):
            if v > y[0][i]:
                return 1
            elif v < y[0][i]:
                return -1
        # They are equal
        return 0

    if left > right:
        return 1
    return -1


def convert_to_value(card: str) -> list[int]:
    return tuple(input_to_value[el] for el in card)


if __name__ == "__main__":
    run_part("07/input.txt", p2, 2)
