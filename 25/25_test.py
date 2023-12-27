import pytest
from common.utils import read_file
from part1 import p1


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "25/test_input.txt", 54, id="Day 25 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected
