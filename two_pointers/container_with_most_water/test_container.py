import pytest
from solution_1 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_one(solution):
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_two(solution):
    assert solution.maxArea([1, 1]) == 1


def test_two_tall_walls_far_apart(solution):
    assert solution.maxArea([10, 1, 1, 1, 10]) == 40


def test_decreasing_heights(solution):
    assert solution.maxArea([5, 4, 3, 2, 1]) == 6


def test_increasing_heights(solution):
    assert solution.maxArea([1, 2, 3, 4, 5]) == 6


def test_all_same_height(solution):
    assert solution.maxArea([3, 3, 3, 3]) == 9


def test_single_pair(solution):
    assert solution.maxArea([5, 7]) == 5