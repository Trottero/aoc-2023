from common.utils import run_part


def p1(input: list[str]) -> int:
    resolutions = []
    grid = []
    for line in input:
        if line == "":
            resolutions.append(find_mirror_point(grid))
            grid = []
            continue

        grid.append(line)

    resolutions.append(find_mirror_point(grid))

    values = []
    for resolution in resolutions:
        if resolution[1] == "horizontal":
            values.append(resolution[0] * 100)
        else:
            values.append(resolution[0])

    return sum(values)


def find_mirror_point(grid: list[str]) -> tuple[int, str]:
    # Vertical Match
    for startx in range(1, len(grid[0])):
        # See if it is mirrored veritcally
        offset = 0
        while True:
            # If we are still in the loop and one of them goes out of bounds, we stop
            if startx - offset - 1 < 0 or startx + offset >= len(grid[0]):
                return (startx, "vertical")

            # Check if both columns are the same
            if all(
                [
                    grid[y][startx - offset - 1] == grid[y][startx + offset]
                    for y in range(len(grid))
                ]
            ):
                offset += 1
                continue

            break

    # Horizontal Match
    for starty in range(1, len(grid)):
        # See if it is mirrored horizontally
        offset = 0
        while True:
            # If we are still in the loop and one of them goes out of bounds, we stop
            if starty - offset - 1 < 0 or starty + offset >= len(grid):
                return (starty, "horizontal")

            # Check if both rows are the same
            if all(
                [
                    grid[starty - offset - 1][x] == grid[starty + offset][x]
                    for x in range(len(grid[0]))
                ]
            ):
                offset += 1
                continue

            break

    raise Exception("No mirror found")


if __name__ == "__main__":
    run_part("13/input.txt", p1, 1)
