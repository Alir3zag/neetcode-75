import pytest
from product_except_self import Solution

solution = Solution().productExceptSelf

class TestProductExceptSelf:

    def test_leetcode_example_1(self):
        assert solution([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_leetcode_example_2(self):
        assert solution([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_two_elements(self):
        assert solution([3, 4]) == [4, 3]

    def test_contains_zero(self):
        assert solution([1, 2, 0, 4]) == [0, 0, 8, 0]

    def test_two_zeros(self):
        assert solution([0, 0, 2, 3]) == [0, 0, 0, 0]

    def test_all_ones(self):
        assert solution([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_negative_numbers(self):
        assert solution([-1, -2, -3, -4]) == [-24, -12, -8, -6]

    def test_single_large_array(self):
        assert solution([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]