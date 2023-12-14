from common.utils import run_part


def p1(input: list[str]) -> int:
    platform = [[char for char in line] for line in input]
    platform = shift_north(platform)

    rock_weights = []
    for y, row in enumerate(platform):
        for col in row:
            if col == "O":
                rock_weights.append(len(platform) - y)

    return sum(rock_weights)


def shift_north(platform: list[list[str]]) -> list[list[str]]:
    shifted = True
    while shifted:
        shifted = False
        for row in range(len(platform) - 1):
            if shifted:
                break
            for col in range(len(platform[row])):
                if platform[row][col] == "." and platform[row + 1][col] == "O":
                    platform[row][col] = "O"
                    platform[row + 1][col] = "."
                    shifted = True

    return platform


if __name__ == "__main__":
    run_part("14/input.txt", p1, 1)
