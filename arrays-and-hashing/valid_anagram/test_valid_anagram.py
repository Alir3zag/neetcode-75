import pytest
from valid_anagram_1 import Solution as Solution1
from valid_anagram_2 import Solution as Solution2
from valid_anagram_3 import Solution as Solution3
from valid_anagram_4 import Solution as Solution4

solutions = [
    Solution1().isAnagram,
    Solution2().isAnagram,
    Solution3().isAnagram,
    Solution4().isAnagram,
]

@pytest.mark.parametrize("solution", solutions)
class TestValidAnagram:

    def test_leetcode_example_1(self, solution):
        assert solution("anagram", "nagaram") == True

    def test_leetcode_example_2(self, solution):
        assert solution("rat", "car") == False

    def test_anagrams(self, solution):
        assert solution("listen", "silent") == True

    def test_not_anagrams(self, solution):
        assert solution("hello", "world") == False

    def test_different_lengths(self, solution):
        assert solution("abc", "ab") == False

    def test_empty_strings(self, solution):
        assert solution("", "") == True

    def test_case_sensitivity(self, solution):
        assert solution("Dormitory", "DirtyRoom") == False

    def test_single_char_match(self, solution):
        assert solution("a", "a") == True

    def test_single_char_no_match(self, solution):
        assert solution("a", "b") == False

    def test_repeated_chars(self, solution):
        assert solution("aab", "baa") == True

    def test_same_chars_different_count(self, solution):
        assert solution("aab", "bab") == False
