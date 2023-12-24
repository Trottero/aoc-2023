from common.utils import run_part
import re

rules = {}

rule_map = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
}


def p1(input: list[str]) -> int:
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

    accepted_parts = []

    for part in input:
        p = {k: int(v) for k, v in zip(
            ['x', 'm', 'a', 's'], re.findall(r"\d+", part))}

        if part_accepted(p):
            accepted_parts.append(p)

    return sum(sum(part.values()) for part in accepted_parts)


def part_accepted(part: dict[str, int]) -> bool:
    curr = 'in'
    while curr not in ['A', 'R']:
        for subrule in rules[curr]:
            if subrule[0] is not None:
                if rule_map[subrule[1]](part[subrule[0]], subrule[2]):
                    curr = subrule[3]
                    break
            else:
                curr = subrule[3]

    return curr == 'A'


if __name__ == "__main__":
    run_part("19/input.txt", p1, 1)
