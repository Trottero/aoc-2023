from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    times = [int(x) for x in re.findall(r"\d+", input[0])]
    distances = [int(x) for x in re.findall(r"\d+", input[1])]
    data = list(zip(times, distances))

    mult = 1
    for race_time, score_to_beat in data:
        # Loop from start to find lower bound
        lower_bound = 1
        while compute_score(race_time, lower_bound) <= score_to_beat:
            lower_bound += 1

        # Loop from end to find upper bound
        upper_bound = race_time - 1
        while compute_score(race_time, upper_bound) <= score_to_beat:
            upper_bound -= 1

        mult *= (upper_bound - lower_bound + 1)

    return mult


def compute_score(race_time: int, hold_time: int) -> int:
    # Score is determined by multiplying the amount of seconds that you held the boat with the time remaining in the race

    return hold_time * (race_time - hold_time)


if __name__ == "__main__":
    run_part("06/input.txt", p1, 1)
