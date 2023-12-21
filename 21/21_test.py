import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part1


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "21/test_input.txt", 16, id="Day 21 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected):
    part1.steps = 6
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "21/test_input.txt", 0, id="Day 21 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
