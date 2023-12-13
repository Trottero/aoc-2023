import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2
import part2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "12/test_input.txt", 21, id="Day 12 Part 1 - Test Input",
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
            "12/test_input.txt", 525152, id="Day 12 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected


@pytest.mark.parametrize(
    "input, groups, expected",
    [
        pytest.param(
            '???.###', [1, 1, 3], 1, id="Day 12 Part 2 - Test Input 1",
        ),
        pytest.param(
            '.??..??...?##.', [1, 1, 3], 4, id="Day 12 Part 2 - Test Input 2",
        ),
        pytest.param(
            '?#?#?#?#?#?#?#?', [1, 3, 1, 6], 1, id="Day 12 Part 2 - Test Input 3",
        ),
        pytest.param(
            '????.#...#...', [4, 1, 1], 1, id="Day 12 Part 2 - Test Input 4",
        ),
        pytest.param(
            '????.######..#####.', [1, 6, 5], 4, id="Day 12 Part 2 - Test Input 5",
        ),
        pytest.param(
            '?###????????', [3, 2, 1], 10, id="Day 12 Part 2 - Test Input 6",
        ),
    ],
)
def test_p2(input, groups, expected):
    # Test cases for p2 function
    assert part2.resolve(input, groups) == expected
