import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part1


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "09/test_input.txt", 114, id="Day 09 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        pytest.param(
            [0, 3, 6, 9, 12, 15], 18, id="Day 09 Part 1 - Test 1",
        ),
        pytest.param(
            [1, 3, 6, 10, 15, 21], 28, id="Day 09 Part 1 - Test 2",
        ),
        pytest.param(
            [10, 13, 16, 21, 30, 45], 68, id="Day 09 Part 1 - Test 3",
        ),
        pytest.param(
            [5, 5, 5], 5, id="Day 09 Part 1 - Same values",
        ),
        pytest.param(
            [5, 5, 5], 5, id="Day 09 Part 1 - Same values",
        ),
    ],
)
def test_line(line, expected):
    # Test cases for solve_line function
    assert part1.solve_line(line) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "09/test_input.txt", 2, id="Day 09 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
