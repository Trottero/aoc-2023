from common.utils import run_part
import re

boxes: dict[int, dict[str, int]] = {i: {} for i in range(256)}


def p2(input: list[str]) -> int:
    instructions = input[0].split(",")
    for ins in instructions:
        label = re.search(r"[a-z]+", ins).group(0)
        box = compute_hash(label)
        # First parse the instruction
        if "-" in ins:
            # Subtract instruction
            if label in boxes[box]:
                boxes[box].pop(label)
            continue

        # Equals
        if "=" in ins:
            _, focal_length = ins.split("=")
            focal_length = int(focal_length)

            boxes[box][label] = focal_length

    focusing_power = []
    # Evaluate the boxes
    for box in boxes:
        if len(boxes[box]) == 0:
            continue
        # Calculate the focal length

        box_base = box + 1
        box_power = []
        for i, focal_str in enumerate(boxes[box].values()):
            box_power.append(box_base * (i + 1) * focal_str)

        focusing_power.append(sum(box_power))

    return sum(focusing_power)


def compute_hash(input: str) -> int:
    converted = [ord(char) for char in input]
    val = 0
    for char in converted:
        val += char
        val *= 17
        val %= 256
    return val


if __name__ == "__main__":
    run_part("15/input.txt", p2, 2)
