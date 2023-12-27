from common.utils import run_part
import re
import numpy as np

minr = 200000000000000
maxr = 400000000000000

# x eq = [vx, 0] [sx]
# y eq = [0, vy] [sy]


def p1(input: list[str]) -> int:
    particles = []
    for line in input:
        vals = list(map(lambda x: int(x),  re.findall(r"[-\d]+", line)))
        particles.append(vals)
        pass

    particles = list(map(to_matrix, particles))

    for i, particlea in enumerate(particles):
        for j, particleb in enumerate(particles):
            if i == j:
                continue

            a1, b1 = particlea
            a2, b2 = particleb

            solution = np.linalg.solve(a1-a2, -b2-b1)
            pass


def to_matrix(particle) -> tuple[np.ndarray, np.ndarray]:
    x, y, z, vx, vy, vz = particle
    return (np.array([np.array([vx, 0], dtype=np.float64), np.array([0, vy], dtype=np.float64)],  dtype=np.float64), -np.array([x, y], dtype=np.float64))


if __name__ == "__main__":
    run_part("24/input.txt", p1, 1)
