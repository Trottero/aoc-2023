from common.utils import run_part
import networkx as nx
import math


def p1(input: list[str]) -> int:
    G = nx.Graph()

    for line in input:
        a, b = line.split(": ")
        for n in b.split(" "):
            G.add_edge(a, n)

    # Compute the highest betweenness centrality
    for _ in range(3):
        node = max(nx.edge_betweenness_centrality(
            G).items(), key=lambda x: x[1])[0]
        G.remove_edge(*node)

    sizes = [len(x) for x in nx.connected_components(G)]
    return math.prod(sizes)


if __name__ == "__main__":
    run_part("25/input.txt", p1, 1)
