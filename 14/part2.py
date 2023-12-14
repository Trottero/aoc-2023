from common.utils import run_part


cache = {}


def p2(input: list[str]) -> int:
    platform = [[char for char in line] for line in input]
    count = 0
    while True:
        key = "".join(["".join(row) for row in platform])
        if key in cache:
            print("Found a cycle!", cache[key])
            break
        else:
            cache[key] = count

        platform = cycle(platform)
        count += 1

    cycle_length = count - cache[key]

    target_length = 1000000000
    cycles_left = (target_length - count) % cycle_length
    print(f"cycles_left: {cycles_left}")

    for _ in range(cycles_left):
        platform = cycle(platform)

    return compute_load(platform)


def compute_load(platform):
    rock_weights = []
    for y, row in enumerate(platform):
        for col in row:
            if col == "O":
                rock_weights.append(len(platform) - y)

    return sum(rock_weights)


def cycle(platform: list[list[str]]) -> list[list[str]]:
    platform = shift_north(platform)
    platform = shift_west(platform)
    platform = shift_south(platform)
    platform = shift_east(platform)

    return platform


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


def shift_south(platform: list[list[str]]) -> list[list[str]]:
    shifted = True
    while shifted:
        shifted = False
        for row in range(len(platform) - 1, 0, -1):
            if shifted:
                break
            for col in range(len(platform[row])):
                if platform[row][col] == "." and platform[row - 1][col] == "O":
                    platform[row][col] = "O"
                    platform[row - 1][col] = "."
                    shifted = True

    return platform


def shift_west(platform: list[list[str]]) -> list[list[str]]:
    shifted = True
    while shifted:
        shifted = False
        for row in range(len(platform)):
            if shifted:
                break
            for col in range(len(platform[row]) - 1):
                if platform[row][col] == "." and platform[row][col + 1] == "O":
                    platform[row][col] = "O"
                    platform[row][col + 1] = "."
                    shifted = True

    return platform


def shift_east(platform: list[list[str]]) -> list[list[str]]:
    shifted = True
    while shifted:
        shifted = False
        for row in range(len(platform)):
            if shifted:
                break
            for col in range(len(platform[row]) - 1, 0, -1):
                if platform[row][col] == "." and platform[row][col - 1] == "O":
                    platform[row][col] = "O"
                    platform[row][col - 1] = "."
                    shifted = True

    return platform


if __name__ == "__main__":
    run_part("14/input.txt", p2, 2)
