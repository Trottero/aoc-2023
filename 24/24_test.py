import pytest
from common.utils import read_file
import part1
from part2 import p2


@pytest.mark.parametrize(
    "filename, minr, maxr, expected",
    [
        pytest.param(
            "24/test_input.txt", 7, 27, 2, id="Day 24 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, minr, maxr, expected):
    part1.minr = minr
    part1.maxr = maxr
    # Test cases for p1 function
    assert part1.p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "24/test_input.txt", 24, id="Day 24 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
