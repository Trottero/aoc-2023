from common.utils import run_part


minr = 200000000000000
maxr = 400000000000000

# x eq = xstart + vx * t
# y eq = ystart + vy * t
# z eq = zstart + vz * t

# xstart1 + vx1 * t = xstart2 + vx2 * t

# (vx1 - vx2) * t = xstart2 - xstart1
# (vy1 - vy2) * t = ystart2 - ystart1


def p1(input: list[str]) -> int:

    return 0


if __name__ == "__main__":
    run_part("24/input.txt", p1, 1)
