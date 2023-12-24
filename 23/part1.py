from common.utils import run_part
import networkx as nx


def p1(input: list[str]) -> int:
    G: nx.DiGraph = nx.grid_2d_graph(
        len(input), len(input[0]), create_using=nx.DiGraph)

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "#":
                G.remove_node((y, x))
            if char == ">":
                G.remove_edge((y, x + 1), (y, x))
            if char == "<":
                G.remove_edge((y, x - 1), (y, x))
            if char == "v":
                G.remove_edge((y + 1, x), (y, x))
            if char == "^":
                raise NotImplementedError()

    start_pos = (0, input[0].index("."))
    end_pos = (len(input) - 1, input[-1].index("."))

    heaviest_path = max((path for path in nx.all_simple_paths(G, start_pos, end_pos)),
                        key=lambda p: len(p))

    grid = [[x for x in row] for row in input]
    for y, x in heaviest_path:
        grid[y][x] = "O"

    print_grid(grid)

    assert len(heaviest_path) == len(set(heaviest_path))

    return len(heaviest_path) - 1


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


if __name__ == "__main__":
    run_part("23/input.txt", p1, 1)
