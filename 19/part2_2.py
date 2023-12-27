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

    # Prayge that the rules are exclusive.

    ranges = resolve_rule('int', {'x': range(1, 4001), 'm': range(
        1, 4001), 'a': range(1, 4001), 's': range(1, 4001)})


def resolve_rule(rulekey: str, constraints: dict[str, range]) -> dict[str, range]:
    subrules = rules[rulekey]
    for i, (left, op, right, dest) in enumerate(subrules):
        if dest != 'A':
            continue


if __name__ == "__main__":
    run_part("19/input.txt", p2, 2)
