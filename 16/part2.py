from common.utils import run_part
import tqdm


class Beam:
    def __init__(self, pos: tuple[int, int], dir: tuple[int, int]):
        self.pos = pos
        self.dir = dir

    def step(self) -> None:
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])


class Grid:
    def __init__(self, input: list[list[str]]) -> None:
        self.grid = input.copy()
        self.energized = {}

    def at(self, y: int, x: int) -> tuple[str, bool]:
        return self.grid[y][x]

    def energize(self, y: int, x: int, dir: tuple[int, int]) -> bool:
        if (y, x) not in self.energized:
            self.energized[(y, x)] = {}

        if dir not in self.energized[(y, x)]:
            self.energized[(y, x)][dir] = True
            return True

        return False

    def in_bounds(self, y: int, x: int) -> bool:
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0])

    def count_energized(self) -> int:
        return len(self.energized.keys())

    def get_energized_grid(self) -> list[list[str]]:
        grid = [['.' for c in line] for line in self.grid]
        for y, x in self.energized:
            grid[y][x] = "#"
        return grid


def p2(input: list[str]) -> int:
    grid = Grid([[c for c in line] for line in input])
    beams_configs = []
    for y in range(len(grid.grid)):
        beams_configs.append(Beam((y, -1), (0, 1)))
        beams_configs.append(Beam((y, len(grid.grid)), (0, -1)))
        pass

    for x in range(len(grid.grid[0])):
        beams_configs.append(Beam((-1, x), (1, 0)))
        beams_configs.append(Beam((len(grid.grid[0]), x), (-1, 0)))

    results = []
    for config in tqdm.tqdm(beams_configs):
        results.append(get_configuration_energy(config, grid))

    return max(results)


def get_configuration_energy(b: Beam, grid: Grid) -> int:
    beams = [b]
    g = Grid(grid.grid)
    new_energized = True
    while beams and new_energized:
        new_energized = False
        new_beams = []
        for beam in beams:
            new_beam, energized = step(g, beam)
            new_energized = new_energized or energized
            new_beams.extend(new_beam)

        beams = new_beams.copy()

    return g.count_energized()


def step(grid: Grid, beam: Beam) -> tuple[list[Beam], bool]:
    # Perform step in direction
    beam.step()

    beamy, beamx = beam.pos
    # If out of range, return empty list
    if not grid.in_bounds(beamy, beamx):
        return [], False

    # Mark energized
    energized = grid.energize(beamy, beamx, beam.dir)

    if not energized:
        return [], False

    if grid.at(beamy, beamx) == ".":
        return [beam], energized

    # Handle splits
    if grid.at(beamy, beamx) == "|":
        if beam.dir == (1, 0) or beam.dir == (-1, 0):
            return [beam], energized
        return [Beam(beam.pos, (1, 0)), Beam(beam.pos, (-1, 0))], energized

    if grid.at(beamy, beamx) == "-":
        if beam.dir == (0, 1) or beam.dir == (0, -1):
            return [beam], energized
        return [Beam(beam.pos, (0, 1)), Beam(beam.pos, (0, -1))], energized

    # Handle mirrors
    if grid.at(beamy, beamx) == "/":
        dy, dx = beam.dir
        return [Beam(beam.pos, (-dx, -dy))], energized

    if grid.at(beamy, beamx) == "\\":
        dy, dx = beam.dir
        return [Beam(beam.pos, (dx, dy))], energized

    raise Exception("Invalid character")


if __name__ == "__main__":
    run_part("16/input.txt", p2, 2)
