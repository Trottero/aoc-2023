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

    count = 0

    for i, particlea in enumerate(particles):
        for j, particleb in enumerate(particles):
            if i == j:
                continue

            a1, b1 = particlea
            a2, b2 = particleb

            A = np.vstack([b1, -b2]).T
            B = a2-a1
            det = np.linalg.det(A)
            if det == 0:
                continue
            solution = np.linalg.solve(A, B)
            if solution[0] < 0 or solution[1] < 0:
                continue
            x = b1[0] * solution[0] + a1[0]
            y = b2[1] * solution[1] + a2[1]

            if x > minr and x < maxr and y > minr and y < maxr:
                count += 1

            pass

    return count / 2


def to_matrix(particle) -> tuple[np.ndarray, np.ndarray]:
    x, y, z, vx, vy, vz = particle
    return (np.array([x, y], dtype=np.float64), np.array([vx, vy], dtype=np.float64))


if __name__ == "__main__":
    run_part("24/input.txt", p1, 1)
