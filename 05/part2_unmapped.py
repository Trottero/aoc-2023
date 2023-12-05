import re
from common.utils import run_part


def p2(input: list[str]) -> int:
    seeds = input.pop(0)
    seeds = re.findall(r"\d+", seeds)

    new_seeds = []
    for i in range(0, len(seeds), 2):
        start, x = seeds[i: i + 2]
        new_seeds.append((int(start), int(x)))
    seeds = new_seeds
    _ = input.pop(0)

    projection_map = []

    # Construct projection map
    while len(input) > 0:
        mapping_config = input.pop(0)
        mapping_config, _ = mapping_config.split(" ")

        mapping_rule = []
        while len(input) > 0 and input[0] != "":
            rule = input.pop(0)
            target, src, length = re.findall(r"\d+", rule)
            mapping_rule.append((int(src), int(target), int(length)))

        projection_map.append((mapping_config, mapping_rule))

        # Discard empty line
        if len(input) > 0:
            input.pop(0)

    values = seeds.copy()
    for _, mapping_rules in projection_map:
        values = [map_range(start, length, mapping_rules)
                  for start, length in values]
        # Unpack values
        values = [x for sublist in values for x in sublist]

    return min(x[0] for x in values)


def map_range(a_start: int, a_length: int, mapping_rules: list[tuple[int, int, int]]) -> list[int]:
    # Split ranged based on mapping rules
    new_ranges = split_range(a_start, a_length, mapping_rules)

    # Apply mapping rules
    for i, (a, e) in enumerate(new_ranges):
        new_ranges[i] = (map_fn(a, mapping_rules), e)

    return new_ranges


def map_fn(number: int, mapping_rules: list[tuple[int, int, int]]) -> int:
    # Mapping rules are src, target, length
    for src, target, length in mapping_rules:
        if number >= src and number <= src + length:
            return target + (number - src)

    return number


def split_range(a_start: int, a_length: int, mapping_rules: list[tuple[int, int, int]]) -> list[int]:
    # Split incoming range such that mapping rules can be applied with confidence that they will not overflow into other rules.

    new_ranges = []
    # We need to check the following things:

    for rule_src, rule_offset, rule_length in mapping_rules:
        # Range is before rule
        if a_start + a_length <= rule_src:
            continue

        # Range is after rule
        if a_start >= rule_src + rule_length:
            continue

        # Range is fully contained in rule, this results in 1 new rule
        if a_start >= rule_src and a_start + a_length <= rule_src + rule_length:
            new_ranges.append((a_start, a_length))
            continue

        # Rule only contains a subset of the range, this results in 3 new rules
        if a_start <= rule_src and a_start + a_length >= rule_src + rule_length:
            # Middle side (projected)
            new_ranges.append((rule_src, rule_length))
            continue

        # Rule overlaps with the left side of the range, this results in 2 new rules
        if a_start <= rule_src and a_start + a_length <= rule_src + rule_length and a_start + a_length > rule_src:
            # Middle side (projected)
            new_ranges.append((rule_src, a_start + a_length - rule_src))
            continue

        # Rule overlaps with the right side of the range, this results in 2 new rules
        if a_start >= rule_src and a_start + a_length >= rule_src + rule_length and a_start < rule_src + rule_length:
            a = a_start + a_length - rule_src - rule_length
            new_ranges.append(
                (rule_src + (a_start - rule_src), a_length - a))
            continue
        raise Exception("Unhandled case")

    # Filter out all the ranges that have a length of 0
    new_ranges = [x for x in new_ranges if x[1] > 0]

    # Convert

    # Does any mapping rule affect the range at all?
    if len(new_ranges) == 0:
        new_ranges = [(a_start, a_length)]

    return new_ranges


if __name__ == "__main__":
    run_part("05/input.txt", p2, 2)
