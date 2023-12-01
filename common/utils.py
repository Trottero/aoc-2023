import time


def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]


def run_day(file_path, fn1, fn2):
    run_part(file_path, fn1, 1)
    run_part(file_path, fn2, 2)


def run_part(file_path: str, fn, part: int):
    input = read_file(file_path)
    # Start Timer for Part 1
    start = time.time()
    res = fn(input)
    end = time.time()
    print(f'Part {part} result:')
    print(res)
    print(f"Part {part} took {end - start} seconds")
