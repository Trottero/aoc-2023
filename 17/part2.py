from common.utils import run_part


class Node:
    def __init__(self, position: tuple[int, int], direction: tuple[int, int], path_length: int, parent: "Node" = None) -> None:
        self.position = position
        self.direction = direction
        self.parent = parent
        self.path_length = path_length

    def __str__(self) -> str:
        return f"node({self.position}{self.direction}{self.path_length})"

    def get_neighbors(self, grid: list[list[int]]) -> list["Node"]:
        y, x = self.position
        dy, dx = self.direction
        neighbors = []

        if self.path_length < 3:
            new_coord = (y + dy, x + dx)
            # Check if in bounds
            if 0 <= new_coord[0] < len(grid) and 0 <= new_coord[1] < len(grid[new_coord[0]]):
                return [Node((y + dy, x + dx), self.direction, self.path_length + 1, self)]
            else:
                return []

        if y > 0 and self.direction != (1, 0):
            if self.direction != (-1, 0):
                neighbors.append(
                    Node((y - 1, x), (-1, 0), 0, self))
            elif self.path_length < 9:
                neighbors.append(
                    Node((y - 1, x), (-1, 0), self.path_length + 1, self))

        if y < len(grid) - 1 and self.direction != (-1, 0):
            if self.direction != (1, 0):
                neighbors.append(
                    Node((y + 1, x), (1, 0), 0, self))
            elif self.path_length < 9:
                neighbors.append(
                    Node((y + 1, x), (1, 0), self.path_length + 1, self))
        if x > 0 and self.direction != (0, 1):
            if self.direction != (0, -1):
                neighbors.append(
                    Node((y, x - 1), (0, -1), 0, self))
            elif self.path_length < 9:
                neighbors.append(
                    Node((y, x - 1), (0, -1), self.path_length + 1, self))
        if x < len(grid[y]) - 1 and self.direction != (0, -1):
            if self.direction != (0, 1):
                neighbors.append(
                    Node((y, x + 1), (0, 1), 0, self))
            elif self.path_length < 9:
                neighbors.append(
                    Node((y, x + 1), (0, 1), self.path_length + 1, self))

        return neighbors


def p2(input: list[str]) -> int:
    grid = [[int(c) for c in line] for line in input]

    length, node = dijkstra(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))

    path = resolve_path(node)
    print_grid_path(grid, path)

    return length


def dijkstra(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    start_nodes = [Node(start, (1, 0), 0), Node(start, (0, 1), 0)]
    open_set: dict[str, tuple[Node, int]] = {
        str(node): (node, 0) for node in start_nodes}

    closed_set: dict[str, tuple[Node, int]] = {}

    shorted_path_length = None
    end_node = None

    while open_set:
        if shorted_path_length is not None:
            # If we have a shorted path, we can stop searching
            if min(x[1] for x in open_set.values()) > shorted_path_length:
                break

        # Get min by current cost
        h, (node, cost) = min(open_set.items(), key=lambda c: c[1][1])
        open_set.pop(h)

        # Add to closed set
        closed_set[h] = (node, cost)

        if node.position == end and node.path_length > 2:
            # We found the end
            if shorted_path_length is None or cost <= shorted_path_length:
                shorted_path_length = cost
                end_node = node
            continue

        for neighbor in node.get_neighbors(grid):
            traverse_cost = grid[neighbor.position[0]][neighbor.position[1]]
            if str(neighbor) not in closed_set and str(neighbor) not in open_set:
                open_set[str(neighbor)] = (neighbor, cost + traverse_cost)
            elif str(neighbor) in closed_set and cost + traverse_cost < closed_set[str(neighbor)][1]:
                # Also override the parent
                neighbor.parent = node
                closed_set[str(neighbor)] = (neighbor, cost + traverse_cost)
            elif str(neighbor) in open_set and cost + traverse_cost < open_set[str(neighbor)][1]:
                # Also override the parent
                neighbor.parent = node
                open_set[str(neighbor)] = (neighbor, cost + traverse_cost)

    return shorted_path_length, end_node


def resolve_path(node: Node) -> list[Node]:
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]


def print_grid_path(grid: list[list[int]], path: list[Node]) -> None:
    g_copy = [line[:] for line in grid]

    direction_map = {
        (1, 0): "v",
        (-1, 0): "^",
        (0, 1): ">",
        (0, -1): "<",
    }

    for node in path:
        g_copy[node.position[0]][node.position[1]
                                 ] = direction_map[node.direction]

    for line in g_copy:
        print("".join(str(c) for c in line))


if __name__ == "__main__":
    run_part("17/input.txt", p2, 2)
