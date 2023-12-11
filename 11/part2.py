from common.utils import run_part
import networkx as nx


def p2(input: list[str]) -> int:
   # First find all of the galaxies and store them in a networkx graph
    galaxies = []
    for y, row in enumerate(input):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((y, x))

    # Precompute which indices are empty rows / columns
    empty_rows = [row_empty(input, y) for y in range(len(input))]
    empty_cols = [col_empty(input, x) for x in range(len(input[0]))]

    G: nx.Graph = nx.complete_graph(galaxies)
    for e in G.edges:
        man = manhattan_distance(*e)

        (src_y, src_x), (target_y, target_x) = e
        empty_row_count = len(list(y for y in range(
            min(src_y, target_y), max(src_y, target_y)) if empty_rows[y]))
        empty_col_count = len(list(x for x in range(
            min(src_x, target_x), max(src_x, target_x)) if empty_cols[x]))

        empty_row_count = empty_row_count * 1000000 - empty_row_count
        empty_col_count = empty_col_count * 1000000 - empty_col_count
        G.edges[e]['weight'] = man + empty_row_count + empty_col_count
    # Distance between galaxies is the Manhattan distance + the adjustment of empty rows / columns

    return sum(G.edges[e]['weight'] for e in G.edges)


def manhattan_distance(src: tuple[int, int], target: tuple[int, int]) -> int:
    return abs(src[0] - target[0]) + abs(src[1] - target[1])


def row_empty(input: list[str], row: int) -> bool:
    return not any([cell == "#" for cell in input[row]])


def col_empty(input: list[str], col: int) -> bool:
    return not any([row[col] == "#" for row in input])


if __name__ == "__main__":
    run_part("11/input.txt", p2, 2)
