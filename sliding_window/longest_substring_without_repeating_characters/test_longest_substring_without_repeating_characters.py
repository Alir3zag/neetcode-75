import pytest
from longest_substring_without_repeating_characters import Solution

solution = Solution().lengthOfLongestSubstring

class TestLengthOfLongestSubstring:

    def test_leetcode_example_1(self):
        assert solution("abcabcbb") == 3

    def test_leetcode_example_2(self):
        assert solution("bbbbb") == 1

    def test_leetcode_example_3(self):
        assert solution("pwwkew") == 3

    def test_empty_string(self):
        assert solution("") == 0

    def test_single_char(self):
        assert solution("a") == 1

    def test_all_unique(self):
        assert solution("abcdef") == 6

    def test_spaces(self):
        assert solution("a b c") == 3

    def test_numbers(self):
        assert solution("123123") == 3
