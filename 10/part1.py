from common.utils import run_part


input_map: dict[str, dict[tuple[int, int], tuple[int, int]]] = {
    "-": {
        (0, 1): (0, 1),
        (0, -1): (0, -1),
    },
    "|": {
        (-1, 0): (-1, 0),
        (1, 0): (1, 0),
    },
    "L": {
        (1, 0): (0, 1),
        (0, -1): (-1, 0)
    },
    "J": {
        (1, 0): (0, -1),
        (0, 1): (-1, 0)
    },
    "7": {
        (0, 1): (1, 0),
        (-1, 0): (0, -1)
    },
    "F": {
        (0, -1): (1, 0),
        (-1, 0): (0, 1)
    },
}


def p1(input: list[str]) -> int:
    grid = [list(line) for line in input]
    y, x = find_animal(grid)
    # Find the first valid pipe piece around the animal.
    direction = find_valid_pipe(grid, y, x)
    y += direction[0]
    x += direction[1]

    performed_steps = 1
    y, x, direction = perform_step(grid, y, x, direction)
    while grid[y][x] != "S":
        performed_steps += 1
        y, x, direction = perform_step(grid, y, x, direction)
    return (performed_steps + 1) / 2


def find_valid_pipe(grid, y, x) -> tuple[int, int]:
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in deltas:
        pipe = grid[y + dy][x + dx]
        if pipe == '.':
            continue
        for direction in input_map[pipe]:
            if direction == (dy, dx):
                return direction


def perform_step(grid, y, x, previous_dir) -> tuple[int, int, tuple[int, int]]:
    current_pipe = grid[y][x]
    next_step = input_map[current_pipe][previous_dir]

    # Apply the next step
    y += next_step[0]
    x += next_step[1]

    return y, x, next_step


def find_animal(grid) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                return (y, x)


if __name__ == "__main__":
    run_part("10/input.txt", p1, 1)
