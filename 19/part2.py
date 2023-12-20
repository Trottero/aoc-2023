from common.utils import run_part
import re
from itertools import product

rules = {}

rule_map = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
}


def p2(input: list[str]) -> int:
    while input[0] != "":
        rule = re.search(r"[{](.*)[}]", input[0])
        rule_id = input[0].split("{")[0]
        subrules = rule.group(1).split(",")
        processed = []
        for subrule in subrules:
            sm = re.search(r"([xmas])([<>])(\d+):([a-zAR]+)", subrule)
            if sm is not None:
                var = sm.group(1)
                op = sm.group(2)
                val = int(sm.group(3))
                dest = sm.group(4)

                processed.append((var, op, val, dest))
                continue

            processed.append((None, None, None, subrule))

        rules[rule_id] = processed.copy()

        input.pop(0)
    input.pop(0)

    letter_counts = {
        'x': [],
        'm': [],
        'a': [],
        's': [],
    }

    for letter in letter_counts.keys():
        for i in range(1, 4001):
            if part_accepted({letter: i}, letter):
                letter_counts[letter].append(i)

    return len(letter_counts['x']) * len(letter_counts['m']) * len(letter_counts['a']) * len(letter_counts['s'])


def part_accepted(part: dict[str, int], piece: str, curr='in') -> bool:
    ncurr = curr
    if ncurr in ['A', 'R']:
        return ncurr == 'A'

    for left, op, right, dest in rules[ncurr]:
        if left is not piece:
            continue

        if rule_map[op](part[left], right):
            return part_accepted(part, piece, dest)
        return False

    # If not in the rules, then we give it free pass for this depth
    return any(part_accepted(part, piece, a[3]) for a in rules[ncurr])


if __name__ == "__main__":
    run_part("19/input.txt", p2, 2)

183808000000000
167409079868000
