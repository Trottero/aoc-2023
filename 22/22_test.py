import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part1


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "22/test_input.txt", 5, id="Day 22 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(
            range(1, 1), range(1, 1), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            range(1, 1), range(1, 2), True, id="Day 22 Part 1 - Test Input 2",
        ),
    ],
)
def test_overlap(a, b, expected):
    assert part1.range_overlap(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(
            (1, 1, 2, 1, 1, 2), (1, 1, 1, 1, 1, 1), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 2, 2, 1, 2), (1, 1, 1, 1, 1, 1), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 2, 3, 1, 2), (1, 1, 1, 1, 1, 1), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (2, 1, 2, 3, 1, 2), (1, 1, 1, 1, 1, 1), False, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 3, 1, 1, 3), (1, 1, 1, 1, 1, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 3, 1, 1, 3), (1, 1, 1, 10, 1, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (2, 1, 3, 12, 1, 3), (1, 1, 1, 10, 1, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (2, 1, 3, 10, 1, 3), (1, 1, 1, 10, 1, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (10, 1, 3, 10, 1, 3), (1, 1, 1, 10, 1, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (11, 1, 3, 12, 1, 3), (1, 1, 1, 10, 1, 2), False, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (2, 1, 3, 10, 1, 3), (1, 1, 1, 1, 10, 2), False, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 3, 10, 1, 3), (1, 1, 1, 1, 10, 2), True, id="Day 22 Part 1 - Test Input 1",
        ),
        pytest.param(
            (1, 1, 4, 10, 1, 4), (1, 1, 1, 1, 10, 2), False, id="Day 22 Part 1 - Test Input 1",
        ),
    ],
)
def test_rests_on(a, b, expected):
    assert part1.bricka_rests_on_b(a, b) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "22/test_input.txt", 7, id="Day 22 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
