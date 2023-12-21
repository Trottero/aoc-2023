from common.utils import run_part
import networkx as nx

steps = 64


def p1(input: list[str]) -> int:
    xlen = len(input[0])
    ylen = len(input)
    G: nx.Graph = nx.grid_2d_graph(ylen, xlen)

    start_pos = (0, 0)
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "#":
                G.remove_node((y, x))
            elif char == "S":
                start_pos = (y, x)

    paths = nx.single_source_shortest_path_length(G, start_pos, steps)

    return len([1 for p in paths.values() if p % 2 == 0])


if __name__ == "__main__":
    run_part("21/input.txt", p1, 1)
