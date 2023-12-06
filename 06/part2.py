import re
from common.utils import run_part


def p2(input: list[str]) -> int:
    times = int("".join(re.findall(r"\d+", input[0])))
    distances = int("".join(re.findall(r"\d+", input[1])))

    # Loop from start to find lower bound
    lower_bound = 1
    while compute_score(times, lower_bound) <= distances:
        lower_bound += 1

    # Loop from end to find upper bound
    upper_bound = times - 1
    while compute_score(times, upper_bound) <= distances:
        upper_bound -= 1

    return (upper_bound - lower_bound + 1)


def compute_score(race_time: int, hold_time: int) -> int:
    # Score is determined by multiplying the amount of seconds that you held the boat with the time remaining in the race

    return hold_time * (race_time - hold_time)


if __name__ == "__main__":
    run_part("06/input.txt", p2, 2)
