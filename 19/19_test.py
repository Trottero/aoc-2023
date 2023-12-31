import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part2_2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "19/test_input.txt", 19114, id="Day 19 Part 1 - Test Input",
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
            "19/test_input.txt", 167409079868000, id="Day 19 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert part2_2.p2(read_file(filename)) == expected
