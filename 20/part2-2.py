from common.utils import run_part
import re
import math

in_out = {}

module_type = {}

conj_memory = {}
flop_memory = {}

module_dependencies = {}

state = {}

# Assume every conjunction module has a loop
loops = {}

cycles = {}


def p2(input: list[str]) -> int:
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
            loops[k] = [(False, 0)]
        if module_type[k] == "&":
            conj_memory[k] = {dep: False for dep in v}

    c = 0
    while True:
        done = simulate_press()
        c += 1
        # Observe the state of all conjunctions and see if they have changed
        to_rm = []
        for k, v in loops.items():
            if module_type[k] == "%":
                if v[-1][0] != flop_memory[k]:
                    v.append((flop_memory[k], c))
                if len(v) > 4:
                    # cycles[k] = v[-1][1] - v[-3][1]
                    cycles[k] = v[2][1]
                    print(k, cycles[k], v)
                    to_rm.append(k)

        for k in to_rm:
            loops.pop(k)

        if len(loops) == 0:
            print("found all cycles")
            break

    cycles['broadcaster'] = 1
    # Filter the "&"
    cleared_deps = {
        k: v for k, v in module_dependencies.items() if module_type[k] == "&"}

    while len(cleared_deps) > 0:
        to_rm = []
        for k, v in cleared_deps.items():
            # Check if we can resolve this entire conjunction
            if all(sv in cycles for sv in v):
                # This module repeats every n cycles
                n = max([cycles[sv] for sv in v])
                cycles[k] = n
                to_rm.append(k)
        for k in to_rm:
            cleared_deps.pop(k)

    return math.lcm(*[v for k, v in cycles.items() if module_type[k] == "&"])


def simulate_press() -> bool:
    to_eval = [(None, False, 'broadcaster')]
    while len(to_eval) > 0:
        from_, pulse, to_ = to_eval.pop(0)
        if not pulse and to_ == 'rx':
            return True

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

    return False


if __name__ == "__main__":
    run_part("20/input.txt", p2, 2)
