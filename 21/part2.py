from common.utils import run_part

steps = 26501365


def p2(input: list[str]) -> int:
    grid = [list(line) for line in input]
    # Find S in grid
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "S":
                grid_values = {(y, x): 1}
                break

    for _ in range(steps):
        new_grid_values = {}
        for pos, value in grid_values.items():
            pass
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = pos[1] + dx
                if nx < 0:
                    nx = len(grid[0]) - 1
                elif nx >= len(grid[0]):
                    nx = 0
                ny = pos[0] + dy
                if ny < 0:
                    ny = len(grid) - 1
                elif ny >= len(grid):
                    ny = 0

                new_pos = (ny, nx)
                if grid[new_pos[0]][new_pos[1]] == "#":
                    continue
                if new_pos not in new_grid_values:
                    new_grid_values[new_pos] = 0
                new_grid_values[new_pos] += value

        grid_values = new_grid_values.copy()
        pass

    return sum(grid_values.values())


if __name__ == "__main__":
    run_part("21/input.txt", p2, 2)
