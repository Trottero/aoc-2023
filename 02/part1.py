from common.utils import run_part
import re

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def p1(input: list[str]) -> int:
    valid_games = []
    for game in input:
        gameid = re.search(r"\d+", game).group(0)
        rounds = game.split(':')[1].strip()

        valid_game = all([is_valid_round(r) for r in rounds.split(';')])

        if valid_game:
            valid_games.append(int(gameid))

    return sum(valid_games)


def is_valid_round(round: str) -> bool:
    draws = [s.strip().split() for s in round.split(',')]

    # Check if all the draws do not exceed the maxes
    return all([int(d[0]) <= maxes[d[1]] for d in draws])


if __name__ == "__main__":
    run_part("02/input.txt", p1, 1)
