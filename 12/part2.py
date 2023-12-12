from common.utils import run_part
import re


def p2(input: list[str]) -> int:
    vals = []
    searched = []
    for line in input:
        row, groups = line.split(" ")
        row = row * 5
        groups = groups * 5
        groups = [int(x) for x in groups.split(",")]
        tests = ['']
        searched.append(row.count("?") * 2)
        for c in row:
            if c != "?":
                tests = [test + c for test in tests]
            else:
                tests = [test + "#" for test in tests] + \
                    [test + "." for test in tests]

        reg = f"^[.]*{'[.]+'.join(['#'*x for x in groups])}[.]*$"
        vals.append(sum([1 for test in tests if is_valid(test, reg)]))
    print('searched: ', sum(searched))
    return sum(vals)


def resolve(remainder: str, groups: list[int]) -> int:
    if len(groups) == 0 and remainder.count("#") == 0:
        return 1  # Valid combination

    # Validate if this group fits with the left over groups
    vague_group = re.search(r"[#?]+", remainder)
    if not vague_group:
        return 0  # Invalid combination

    vague_group_size = len(vague_group.group(0))
    groups_to_process = groups.copy()
    expected_group_size = groups_to_process.pop(0)

    # Check if the group fits at all
    if expected_group_size > vague_group_size:
        return 0  # Invalid combination

    start_match = re.search(r"^#+", remainder[vague_group.start():])
    broken_start_count = len(re.search())


def is_valid(test: str, regex: str) -> bool:
    return re.search(regex, test) is not None


if __name__ == "__main__":
    run_part("12/input.txt", p2, 2)
