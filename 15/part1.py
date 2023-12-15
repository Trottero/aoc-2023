from common.utils import run_part


def p1(input: list[str]) -> int:
    strs = input[0].split(",")

    return sum([compute_hash(string) for string in strs])


def compute_hash(input: str) -> int:
    converted = [ord(char) for char in input]
    val = 0
    for char in converted:
        val += char
        val *= 17
        val %= 256
    return val


if __name__ == "__main__":
    run_part("15/input.txt", p1, 1)
