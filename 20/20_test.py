import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "20/test_input_1.txt", 32000000, id="Day 20 Part 1 - Test Input 1",
        ),
        pytest.param(
            "20/test_input_2.txt", 11687500, id="Day 20 Part 1 - Test Input 2",
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
            "20/test_input_2.txt", 0, id="Day 20 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
