import time


def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]


def run_day(file_path, fn1, fn2):
    input = read_file(file_path)
    # Start Timer for Part 1
    start = time.time()
    res1 = fn1(input)
    end = time.time()
    print(f'Part 1 result:')
    print(res1)
    print(f"Part 1 took {end - start} seconds")

    # Start Timer for Part 2
    start2 = time.time()
    res2 = fn2(input)
    end2 = time.time()
    print(f'Part 2 result:')
    print(res2)
    # Print Results
    print(f"Part 2 took {end2 - start2} seconds")
