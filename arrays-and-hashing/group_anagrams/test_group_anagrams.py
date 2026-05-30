import pytest
from group_anagrams import Solution

solution = Solution().groupAnagrams

def sorted_result(result):
    return sorted([sorted(group) for group in result])

class TestGroupAnagrams:

    def test_leetcode_example_1(self):
        result = solution(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert sorted_result(result) == sorted_result([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    def test_leetcode_example_2(self):
        assert solution([""]) == [[""]]

    def test_leetcode_example_3(self):
        assert solution(["a"]) == [["a"]]

    def test_all_anagrams(self):
        result = solution(["abc", "bca", "cab"])
        assert sorted_result(result) == [["abc", "bca", "cab"]]

    def test_no_anagrams(self):
        result = solution(["abc", "def", "ghi"])
        assert sorted_result(result) == [["abc"], ["def"], ["ghi"]]

    def test_single_word(self):
        assert solution(["hello"]) == [["hello"]]

    def test_duplicate_words(self):
        result = solution(["abc", "abc"])
        assert sorted_result(result) == [["abc", "abc"]]

    def test_mixed_lengths(self):
        result = solution(["a", "ab", "ba"])
        assert sorted_result(result) == [["a"], ["ab", "ba"]]

    def test_empty_strings(self):
        result = solution(["", "", ""])
        assert sorted_result(result) == [["", "", ""]]