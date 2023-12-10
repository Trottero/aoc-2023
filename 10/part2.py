from common.utils import run_part
import sys
sys.setrecursionlimit(100_000)

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


def p2(input: list[str]) -> int:
    grid = [list(line) for line in input]
    y, x = find_animal(grid)
    main_loop_positions = [(y, x)]
    # Find the first valid pipe piece around the animal.
    direction = find_valid_pipe(grid, y, x)
    first_dir = (direction[0], direction[1])

    y += direction[0]
    x += direction[1]
    main_loop_positions.append((y, x))

    performed_steps = 1
    y, x, direction = perform_step(grid, y, x, direction)
    main_loop_positions.append((y, x))
    while grid[y][x] != "S":
        performed_steps += 1
        y, x, direction = perform_step(grid, y, x, direction)
        main_loop_positions.append((y, x))

    # Set all elements in the grid to . except for the main loop
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (y, x) not in main_loop_positions:
                grid[y][x] = "."

    # Overwrite the animal location with an actual pipe
    # Find the pipe piece
    pipe_piece = find_piece(direction, first_dir)
    animal_y, animal_x = main_loop_positions[0]
    grid[animal_y][animal_x] = pipe_piece

    blank_row = ["@"] * len(grid[0])
    # Add a row in between every row
    for row in reversed(range(len(grid))):
        grid.insert(row, blank_row.copy())
    grid.append(blank_row.copy())

    # For every second row, check if the one above and below it has a pipe that should have connected
    for y, row in enumerate(grid):
        if (y + 1) % 2 == 0 or y == 0 or y == len(grid) - 1:
            continue
        for xi in range(len(row)):
            above = grid[y - 1][xi]
            below = grid[y + 1][xi]
            if above in ["|", "7", "F"] and below in ["|", "L", "J"]:
                row[xi] = "|"
        pass

    # Add a column in between every column
    for row in grid:
        for col in reversed(range(len(row))):
            row.insert(col, "@")
        row.append("@")

    # For every second column, check if the one to the left and right of it has a pipe that should have connected
    for y, row in enumerate(grid):
        for xi in range(len(row)):
            if (xi + 1) % 2 == 0 or xi == 0 or xi == len(row) - 1:
                continue
            left = grid[y][xi - 1]
            right = grid[y][xi + 1]
            if left in ["-", "L", "F"] and right in ["-", "J", "7"]:
                row[xi] = "-"

    # Flood fill the grid to find the number of dots
    visited = set()
    y, x = (0, 0)
    filled_dots = flood_fill(grid, y, x, visited)

    # Find the total number of dots
    total_dots = 0
    for row in grid:
        total_dots += row.count(".")

    return total_dots - filled_dots


def flood_fill(grid, y, x, visited) -> int:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return 0

    if (y, x) in visited or grid[y][x] not in ["@", "."]:
        return 0

    visited.add((y, x))

    count = 0
    if grid[y][x] == ".":
        count = 1

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in deltas:
        count += flood_fill(grid, y + dy, x + dx, visited)
    return count


def find_valid_pipe(grid, y, x) -> list[tuple[int, int]]:
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in deltas:
        pipe = grid[y + dy][x + dx]
        if pipe == '.':
            continue
        for direction in input_map[pipe]:
            if direction == (dy, dx):
                return direction


def find_piece(dir, first_dir) -> str:
    for piece in input_map:
        if dir in input_map[piece] and input_map[piece][dir] == first_dir:
            return piece


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
    run_part("10/input.txt", p2, 2)
