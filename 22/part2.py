from common.utils import run_part
import networkx as nx
import tqdm


def p2(input: list[str]) -> int:
    bricks = [line.split("~") for line in input]
    bricks = [tuple(map(lambda x: int(x), b[0].split(
        ",") + b[1].split(","))) + tuple([a]) for b, a in zip(bricks, range(0, len(bricks)))]

    G = nx.DiGraph()
    settled_bricks = {}
    sorted_bricks = sorted(bricks, key=lambda x: x[2])
    for brick in tqdm.tqdm(sorted_bricks):
        # Advance downwards untill x[2] - 1 == 0 or collision with another brick
        # If collision, add to settled_bricks and append to graph

        while not any(bricka_rests_on_b(brick, b) for b in settled_bricks.values()) and brick[2] != 1:
            brick = (brick[0], brick[1], brick[2] -
                     1, brick[3], brick[4], brick[5] - 1, brick[6])

        if brick[2] == 1:
            G.add_edge(brick[6], "ground")
        else:
            for k, v in settled_bricks.items():
                if bricka_rests_on_b(brick, v):
                    G.add_edge(brick[6], k)

        settled_bricks[brick[6]] = brick

    UG = G.copy()

    counts = []
    for n in tqdm.tqdm(UG.nodes):
        if n == "ground":
            continue
        cUG = UG.copy()
        cUG.remove_node(n)

        count = 0
        while any(cUG.out_degree(n) == 0 for n in cUG.nodes if n != "ground"):
            unstable_nodes = [n for n in cUG.nodes if cUG.out_degree(
                n) == 0 and n != "ground"]
            cUG.remove_nodes_from(unstable_nodes)
            count += len(unstable_nodes)

        counts.append(count)

    return sum(counts)


def bricka_rests_on_b(bricka: tuple[int, int, int, int, int, int], brickb: tuple[int, int, int, int, int, int]) -> bool:
    xmatch = range_overlap(
        range(bricka[0], bricka[0 + 3]), range(brickb[0], brickb[0 + 3]))
    ymatch = range_overlap(
        range(bricka[1], bricka[1 + 3]), range(brickb[1], brickb[1 + 3]))
    zmatch = range_overlap(
        range(bricka[2], bricka[2 + 3]), range(brickb[2], brickb[2 + 3] + 1))

    return xmatch and ymatch and zmatch


def range_overlap(range1, range2):
    """Whether range1 and range2 overlap."""
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2


if __name__ == "__main__":
    run_part("22/input.txt", p2, 2)
