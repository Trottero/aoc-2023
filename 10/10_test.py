import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "10/test_input.txt", 4, id="Day 10 Part 1 - Simple loop no BS",
        ),
        pytest.param(
            "10/test_input_simple_bs.txt", 4, id="Day 10 Part 1 - Simple loop with BS",
        ),
        pytest.param(
            "10/test_input_complex.txt", 8, id="Day 10 Part 1 - Complex loop no BS",
        ),
        pytest.param(
            "10/test_input_complex_bs.txt", 8, id="Day 10 Part 1 - Complex loop with BS",
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
            "10/p2/input_1.txt", 4, id="Day 10 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
