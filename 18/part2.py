from common.utils import run_part
import re
import matplotlib.pyplot as plt

from shapely import Polygon, LineString


direction_map = {
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0),
    "U": (0, 1),
}


no_to_dir = {
    0: "R",
    1: "D",
    2: "L",
    3: "U",
}


def p2(input: list[str]) -> int:
    position = (0, 0)
    points = [(0, 0)]
    for line in input:
        matches = re.search(r"^([RDLU])\s(\d+)\s\(#([0-9a-f]{6})\)$", line)
        color = matches.group(3)
        dir = no_to_dir[int(color[-1])]
        dist = int(color[:-1], 16)

        direction = direction_map[dir]
        position = (position[0] + direction[0] *
                    dist, position[1] + direction[1] * dist)

        points.append(position)

    poly = Polygon(points)

    x, y = poly.exterior.xy
    plt.plot(x, y)
    # plt.show()
    print(poly.length / 2 + 1)
    return int(poly.area + poly.length / 2 + 1)


if __name__ == "__main__":
    run_part("18/input.txt", p2, 2)
