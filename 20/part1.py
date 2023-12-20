import re
from common.utils import run_part


in_out = {}

module_type = {}

conj_memory = {}
flop_memory = {}

module_dependencies = {}

state = {}


def p1(input: list[str]) -> int:
    for line in input:
        module, right = line.split(" -> ")
        m_type = re.search(r"[%&]", module)
        module_id = module[1:] if m_type else module
        destinations = right.split(", ")

        in_out[module_id] = destinations
        module_type[module_id] = m_type.group(0) if m_type else None

        for dest in destinations:
            if dest not in module_dependencies:
                module_dependencies[dest] = [module_id]
            else:
                module_dependencies[dest].append(module_id)

            if dest not in module_type:
                module_type[dest] = "b"

    for k, v in module_dependencies.items():
        if module_type[k] == "%":
            flop_memory[k] = False
        if module_type[k] == "&":
            conj_memory[k] = {dep: False for dep in v}

    highs = []
    lows = []
    for i in range(1000):
        hi, low = simulate_press()
        highs.append(hi)
        lows.append(low)

    return sum(highs) * sum(lows)


def simulate_press():
    to_eval = [(None, False, 'broadcaster')]
    lo = 0
    hi = 0
    while len(to_eval) > 0:
        from_, pulse, to_ = to_eval.pop(0)
        if pulse:
            hi += 1
        else:
            lo += 1

        if module_type[to_] is None:
            if to_ not in in_out:
                continue
            for dep in in_out[to_]:
                to_eval.append((to_, False, dep))
            continue

        if module_type[to_] == "%":
            if pulse:
                continue
            flop_memory[to_] = not flop_memory[to_]
            for dep in in_out[to_]:
                to_eval.append((to_, flop_memory[to_], dep))
            continue

        if module_type[to_] == "&":
            conj_memory[to_][from_] = pulse

            next_pulse = not all(conj_memory[to_].values())
            for dep in in_out[to_]:
                to_eval.append((to_, next_pulse, dep))
            continue

    return hi, lo


if __name__ == "__main__":
    run_part("20/input.txt", p1, 1)
