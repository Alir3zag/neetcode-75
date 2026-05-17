import pytest
from three_sum_1 import Solution as TwoPointers
from three_sum_2 import Solution as HashMap


@pytest.fixture(params=[TwoPointers, HashMap])
def solution(request):
    return request.param().threeSum


def test_leetcode_example_1(solution):
    assert sorted(solution([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])


def test_leetcode_example_2(solution):
    assert solution([0, 1, 1]) == []


def test_leetcode_example_3(solution):
    assert solution([0, 0, 0]) == [[0, 0, 0]]


def test_all_negatives(solution):
    assert solution([-4, -3, -2, -1]) == []


def test_all_positives(solution):
    assert solution([1, 2, 3, 4]) == []


def test_duplicates_handled(solution):
    assert sorted(solution([-2, 0, 0, 2, 2])) == sorted([[-2, 0, 2]])


def test_multiple_triplets(solution):
    result = sorted(solution([-4, -1, -1, 0, 1, 2]))
    assert result == sorted([[-1, -1, 2], [-1, 0, 1]])


def test_zeros_only(solution):
    assert solution([0, 0, 0, 0]) == [[0, 0, 0]]