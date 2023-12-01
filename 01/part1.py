from common.utils import run_part


def p1(input: list[str]) -> int:
    digits = []
    for i in input:
        integers = [int(x) for x in i if x.isdigit()]
        digits.append(int(f'{integers[0]}{integers[-1]}'))

    return sum(digits)


if __name__ == "__main__":
    run_part("01/input.txt", p1, 1)
