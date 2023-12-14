from common.utils import run_part
import re
from tqdm.contrib.concurrent import process_map
from itertools import repeat

projection_map = []


def p2(input: list[str]) -> int:
    seeds = input.pop(0)
    seeds = re.findall(r"\d+", seeds)
    _ = input.pop(0)

    new_seeds = []
    for i in range(0, len(seeds), 2):
        seed_start, seed_length = seeds[i: i + 2]
        new_seeds.append((int(seed_start), int(seed_length)))
    seeds = new_seeds

    # Construct projection map
    while len(input) > 0:
        mapping_config = input.pop(0)
        mapping_config, _ = mapping_config.split(" ")

        mapping_rule = []
        while len(input) > 0 and input[0] != "":
            rule = input.pop(0)
            target, src, length = re.findall(r"\d+", rule)
            mapping_rule.append((int(src), int(target), int(length)))

        projection_map.append(mapping_rule)

        # Discard empty line
        if len(input) > 0:
            input.pop(0)

    total_seeds = sum(x[1] for x in seeds)
    print(f'Brute forcing a total of {total_seeds} seeds..')
    # Brute force using TQDM workers

    from tqdm import tqdm, trange
    from multiprocessing import Pool
    from multiprocessing.pool import ThreadPool

    intermediate_results = []

    total_processed = 0

    for i, (seed_start, seed_length) in enumerate(seeds):
        tqdm.write(f'Brute forcing seed {seed_start} ({i+1} / {len(seeds)})..')

        results = process_map(test_seed, range(
            seed_start, seed_start + seed_length), chunksize=1_000, max_workers=16)
        total_processed += len(results)
        intermediate_results.append(min(results))

        tqdm.write(f'Completed! {total_processed /
                                 total_seeds * 100} % processed so far.')

    return min(intermediate_results)


def test_seed(arg) -> int:
    seed = arg
    for projection in projection_map:
        seed = map_fn(seed, projection)

    return seed


def map_fn(number: int, mapping_rules: list[tuple[int, int, int]]) -> int:
    # Mapping rules are src, target, length
    for src, target, length in mapping_rules:
        if number >= src and number < src + length:
            return target + (number - src)

    return number


if __name__ == "__main__":
    run_part("05/input.txt", p2, 2)
