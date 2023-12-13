from common.utils import run_part


def p2(input: list[str]) -> int:
    resolutions = []
    grids: list[list[str]] = []
    grid: list[str] = []

    for line in input:
        if line == "":
            grids.append(grid)
            grid = []
            continue
        grid.append(line)
    grids.append(grid)

    reflection_lines = [find_mirror_point(grid)[0] for grid in grids]

    # Now we are on the quest to modify the grids such that another reflection line appears
    for i, grid in enumerate(grids):
        grid_copy = grid.copy()
        found = False
        for y in range(len(grid)):
            if found:
                break
            for x in range(len(grid[0])):
                if found:
                    break

                # Replace the current y,x with the opposite
                grid_copy[y] = replace_str_index(
                    grid_copy[y], x, flip(grid_copy[y][x]))
                # Evaluate
                potential_reflections = find_mirror_point(grid_copy)
                # Restore
                grid_copy[y] = replace_str_index(
                    grid_copy[y], x, flip(grid_copy[y][x]))

                for reflection in potential_reflections:
                    if reflection != reflection_lines[i]:
                        resolutions.append(reflection)
                        found = True
                        break

    values = []
    for resolution in resolutions:
        if resolution[1] == "horizontal":
            values.append(resolution[0] * 100)
        else:
            values.append(resolution[0])

    return sum(values)


def flip(char: str) -> str:
    if char == '#':
        return '.'
    return '#'


def replace_str_index(text, index=0, replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'


def find_mirror_point(grid: list[str]) -> list[tuple[int, str]]:
    # Vertical Match
    matches = []

    for startx in range(1, len(grid[0])):
        # See if it is mirrored veritcally
        offset = 0
        while True:
            # If we are still in the loop and one of them goes out of bounds, we stop
            if startx - offset - 1 < 0 or startx + offset >= len(grid[0]):
                matches.append((startx, "vertical"))
                break

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
                matches.append((starty, "horizontal"))
                break

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

    return matches


if __name__ == "__main__":
    run_part("13/input.txt", p2, 2)
