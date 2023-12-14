import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "14/test_input.txt", 136, id="Day 14 Part 1 - Test Input",
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
            "14/test_input.txt", 64, id="Day 14 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
