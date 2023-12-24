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
    "filename, steps, expected",
    [
        pytest.param(
            "21/test_input.txt", 6, 16, id="Day 21 Part 2 - Test Input 6",
        ),
        pytest.param(
            "21/test_input.txt", 10, 50, id="Day 21 Part 2 - Test Input 10",
        ),
        pytest.param(
            "21/test_input.txt", 50, 1594, id="Day 21 Part 2 - Test Input 50",
        ),
        pytest.param(
            "21/test_input.txt", 100, 6536, id="Day 21 Part 2 - Test Input 100",
        ),
        pytest.param(
            "21/test_input.txt", 500, 167004, id="Day 21 Part 2 - Test Input 500",
        ),
        pytest.param(
            "21/test_input.txt", 1000, 668697, id="Day 21 Part 2 - Test Input 1000",
        ),
        pytest.param(
            "21/test_input.txt", 5000, 16733044, id="Day 21 Part 2 - Test Input 5000",
        ),
    ],
)
def test_p2(filename, steps, expected):

    import part2
    part2.steps = steps
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
