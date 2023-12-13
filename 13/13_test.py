import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part1


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "13/test_input.txt", 405, id="Day 13 Part 1 - Test Input",
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
            "13/test_files/test-horizontal.txt", (4, "horizontal"), id="Day 13 Part 1 - Test Input Mirror (horizontal)",
        ),
        pytest.param(
            "13/test_files/test-vertical.txt", (5, "vertical"), id="Day 13 Part 1 - Test Input Mirror (vertical)",
        ),
        pytest.param(
            "13/test_files/test-exception.txt", (16, "vertical"), id="Day 13 Part 1 - Test Input Mirror (vertical)",
        ),
    ],
)
def test_find_mirror(filename, expected):
    # Test cases for p1 function
    assert part1.find_mirror_point(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "13/test_input.txt", 400, id="Day 13 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
