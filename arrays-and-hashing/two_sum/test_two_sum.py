import pytest
from two_sum_1 import Solution as Solution1
from two_sum_2 import Solution as Solution2
from two_sum_3 import Solution as Solution3

solutions = [
    Solution1().twoSum,
    Solution2().twoSum,
    Solution3().twoSum,
]

@pytest.mark.parametrize("solution", solutions)
class TestTwoSum:

    def test_leetcode_example_1(self, solution):
        assert solution([2, 7, 11, 15], 9) == [0, 1]

    def test_leetcode_example_2(self, solution):
        assert solution([3, 2, 4], 6) == [1, 2]

    def test_leetcode_example_3(self, solution):
        assert solution([3, 3], 6) == [0, 1]

    def test_answer_not_first_two(self, solution):
        assert solution([1, 2, 3, 4], 7) == [2, 3]

    def test_negative_numbers(self, solution):
        assert solution([-1, -2, -3, -4], -6) == [1, 3]

    def test_mixed_positive_negative(self, solution):
        assert solution([-3, 4, 3, 90], 0) == [0, 2]

    def test_large_input(self, solution):
        nums = list(range(1000))
        assert solution(nums, 1997) == [998, 999]
