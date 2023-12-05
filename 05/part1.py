from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    seeds = input.pop(0)
    seeds = re.findall(r"\d+", seeds)
    _ = input.pop(0)

    projection_map = {}

    # Construct projection map
    while len(input) > 0:
        mapping_config = input.pop(0)
        mapping_config, _ = mapping_config.split(" ")

        mapping_rule = []
        while len(input) > 0 and input[0] != "":
            rule = input.pop(0)
            target, src, length = re.findall(r"\d+", rule)
            mapping_rule.append((int(src), int(target), int(length)))

        projection_map[mapping_config] = mapping_rule

        # Discard empty line
        if len(input) > 0:
            input.pop(0)

    projections = [x for x in projection_map.keys()]
    values = [int(x) for x in seeds]
    for projection in projections:
        mapping_rules = projection_map[projection]
        values = [map_fn(x, mapping_rules) for x in values]

    return min(values)


def map_fn(number: int, mapping_rules: list[tuple[int, int, int]]) -> int:
    # Mapping rules are src, target, length
    for src, target, length in mapping_rules:
        if number >= src and number <= src + length:
            return target + (number - src)

    return number


if __name__ == "__main__":
    run_part("05/input.txt", p1, 1)
