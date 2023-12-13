from common.utils import run_part
import re


def p2(input: list[str]) -> int:
    vals = []
    for line in input:
        row, groups = line.split(" ")
        # row = "?".join([row for _ in range(5)])
        # groups = ",".join([groups for _ in range(5)])
        groups = [int(x) for x in groups.split(",")]

        vals.append(resolve(row, groups))
    return sum(vals)


def resolve(line: str, groups: list[int]) -> int:
    if len(groups) == 0:
        if line.count("#") == 0:
            return 1
        return 0

    # Work on resolving the next group
    gs = groups.copy()
    g = gs.pop(0)

    # Remove all leading dots from the line
    l = line.lstrip(".")

    # Check if even possible after stripping

    if len(l) < g:
        return 0
    subtree_counts = [0]

    if re.match(f"^{'[#?]' * g}", l) is not None and len(gs) == 0:
        # Valid match
        return 1

    # # Check non shifted
    # if re.match(f"^{'[#?]' * g + '[.?]'}", l) is not None:
    #     # Resolve without shifting
    #     subtree_counts.append(resolve(l[g + 1:], gs))

    mat_c = 0
    mat = re.match(f"^{'[#?]' * g}", l)
    r = l
    while mat is not None:
        # Resolve with shifting
        subtree_counts.append(resolve(r[g + mat_c + 1:], gs))
        mat = re.match(f"^[?]{'[#?]' * g}", l[mat_c:])
        mat_c += 1

    return sum(subtree_counts)


if __name__ == "__main__":
    run_part("12/input.txt", p2, 2)
