from common.utils import run_part
import networkx as nx


def p2(input: list[str]) -> int:
    G: nx.DiGraph = nx.grid_2d_graph(
        len(input), len(input[0]), create_using=nx.Graph)

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "#":
                G.remove_node((y, x))

    start_pos = (0, input[0].index("."))
    end_pos = (len(input) - 1, input[-1].index("."))

    # Set all of the weights to 1
    for edge in G.edges:
        G.edges[edge]["weight"] = 1

    # Compress the graph by collapsing all of the nodes that only have 2 edges into a single node
    # This will make the graph much smaller and easier to work with
    print()
    print(f'Before: nodes: {G.number_of_nodes()
                            }, edges: {G.number_of_edges()}')
    # Find all nodes with 2 edges
    nodes_to_collapse = []
    for node in G.nodes:
        if len(G.edges(node)) == 2:
            nodes_to_collapse.append(node)

    # Collapse the nodes
    for node in nodes_to_collapse:
        edges = list(G.edges(node))
        G.add_edge(edges[0][1], edges[1][1], weight=G.edges[edges[0]]
                   ['weight']+G.edges[edges[1]]['weight'])
        G.remove_node(node)

    print(f'After: nodes: {G.number_of_nodes()
                           }, edges: {G.number_of_edges()}')

    longest = 0
    for p in nx.all_simple_edge_paths(G, start_pos, end_pos):
        v = sum(G.edges[i]['weight'] for i in p)
        if v > longest:
            longest = v
            heaviest_path = p
            print(longest)

    # grid = [[x for x in row] for row in input]
    # for y, x in heaviest_path:
    #     grid[y][x] = "O"

    # print_grid(grid)

    # assert len(heaviest_path) == len(set(heaviest_path))

    return longest


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


if __name__ == "__main__":
    run_part("23/input.txt", p2, 2)
