import pytest
from longest_consecutive_sequence import Solution

solution = Solution().longestConsecutive

class TestLongestConsecutiveSequence:

    def test_leetcode_example_1(self):
        assert solution([100, 4, 200, 1, 3, 2]) == 4

    def test_leetcode_example_2(self):
        assert solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    def test_leetcode_example_3(self):
        assert solution([1, 0, 1, 2]) == 3

    def test_empty(self):
        assert solution([]) == 0

    def test_single_element(self):
        assert solution([5]) == 1

    def test_all_duplicates(self):
        assert solution([1, 1, 1, 1]) == 1

    def test_no_consecutive(self):
        assert solution([10, 20, 30]) == 1

    def test_negative_numbers(self):
        assert solution([-3, -2, -1, 0, 1]) == 5