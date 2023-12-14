import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part2
import part2_unmapped
import part2_bruteforce


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "05/test_input.txt", 35, id="Day 05 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "05/test_input.txt", 46, id="Day 05 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "05/test_input.txt", 46, id="Day 05 Part 2 (alt) - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert part2_unmapped.p2(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "05/test_input.txt", 46, id="Day 05 Part 2 (brute force) - Test Input",
        ),
    ],
)
def test_p2_bruteforce(filename, expected):
    # Test cases for p2 function
    assert part2_bruteforce.p2(read_file(filename)) == expected


@pytest.mark.parametrize(
    "in_range, mapping_rules, expected",
    [
        pytest.param(
            (2, 4), [(10, 20, 10)], [(2, 4)], id="Day 05 Part 2 - Dont map",
        ),
        pytest.param(
            (9, 1), [(10, 20, 10)], [(9, 1)], id="Day 05 Part 2 - Dont map (edge left)",
        ),
        pytest.param(
            (20, 2), [(10, 50, 10)], [(20, 2)], id="Day 05 Part 2 - Dont map (edge right)",
        ),
        pytest.param(
            (11, 2), [(10, 20, 10)], [(21, 2)], id="Day 05 Part 2 - Rule contains full range",
        ),
        pytest.param(
            (10, 2), [(10, 20, 10)], [(20, 2)], id="Day 05 Part 2 - Rule contains full range (edge left)",
        ),
        pytest.param(
            (18, 2), [(10, 20, 10)], [(28, 2)], id="Day 05 Part 2 - Rule contains full range (edge right)",
        ),
        pytest.param(
            (10, 10), [(10, 20, 10)], [(20, 10)], id="Day 05 Part 2 - Rule contains full range (full overlap)",
        ),
        pytest.param(
            (5, 15), [(10, 20, 5)], [(5, 5), (20, 5), (15, 5)], id="Day 05 Part 2 - Rule is subset of range",
        ),
        pytest.param(
            (10, 15), [(10, 20, 5)], [(20, 5), (15, 10)], id="Day 05 Part 2 - Rule is subset of range (edge left)",
        ),
        pytest.param(
            (12, 3), [(10, 20, 5)], [(22, 3)], id="Day 05 Part 2 - Rule is subset of range (edge right)",
        ),
        pytest.param(
            (5, 9), [(10, 20, 5)], [(5, 5), (20, 4)], id="Day 05 Part 2 - Range only overlaps left side of rule",
        ),
        pytest.param(
            (12, 10), [(10, 20, 5)], [(22, 3), (15, 7)], id="Day 05 Part 2 - Range only overlaps right side of rule",
        ),
        pytest.param(
            (14, 10), [(10, 20, 5)], [(24, 1), (15, 9)], id="Day 05 Part 2 - Range only overlaps right side of rule (slightly)",
        ),
        pytest.param(
            (5, 6), [(10, 20, 5)], [(5, 5), (20, 1)], id="Day 05 Part 2 - Range only overlaps left side of rule (slightly)",
        ),
    ],
)
def test_p2_map_range(in_range, mapping_rules, expected):
    result = part2.map_range(
        in_range[0], in_range[1], mapping_rules)
    assert result == expected
    assert sum([x[1] for x in result]) == in_range[1]
