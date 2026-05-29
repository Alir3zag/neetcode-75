import pytest
from top_k_frequent_elements import Solution

solution = Solution().topKFrequent

class TestTopKFrequent:

    def test_leetcode_example_1(self):
        assert sorted(solution([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    def test_leetcode_example_2(self):
        assert solution([1], 1) == [1]

    def test_k_equals_all(self):
        assert sorted(solution([1, 2, 3], 3)) == [1, 2, 3]

    def test_all_same(self):
        assert solution([5, 5, 5, 5], 1) == [5]

    def test_negative_numbers(self):
        assert sorted(solution([-1, -1, 2, 2, 3], 2)) == [-1, 2]

    def test_tie_in_frequency(self):
        result = solution([1, 2], 2)
        assert sorted(result) == [1, 2]

    def test_large_k(self):
        assert sorted(solution([1, 1, 2, 2, 3, 3, 4], 3)) == [1, 2, 3]

    def test_single_unique_element(self):
        assert solution([7, 7, 7], 1) == [7]