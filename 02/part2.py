import re
from common.utils import run_part


def p2(input: list[str]) -> int:
    game_powers = []
    for game in input:
        rounds = game.split(':')[1].strip()

        max_draws = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for r in rounds.split(';'):
            draws = [s.strip().split() for s in r.split(',')]
            for d in draws:
                if int(d[0]) > max_draws[d[1]]:
                    max_draws[d[1]] = int(d[0])

        power = max_draws["blue"] * max_draws["green"] * max_draws["red"]
        game_powers.append(power)

    return sum(game_powers)


if __name__ == "__main__":
    run_part("02/input.txt", p2, 2)
