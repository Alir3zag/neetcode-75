import pytest
from valid_palindrome import Solution

solution = Solution().isPalindrome

class TestValidPalindrome:

    def test_leetcode_example_1(self):
        assert solution("A man, a plan, a canal: Panama") == True

    def test_leetcode_example_2(self):
        assert solution("race a car") == False

    def test_leetcode_example_3(self):
        assert solution(" ") == True

    def test_single_char(self):
        assert solution("a") == True

    def test_two_same_chars(self):
        assert solution("aa") == True

    def test_two_diff_chars(self):
        assert solution("ab") == False

    def test_numbers(self):
        assert solution("12321") == True

    def test_mixed_case(self):
        assert solution("Aba") == True

    def test_only_non_alphanumeric(self):
        assert solution(".,!") == True

    def test_alphanumeric_mix(self):
        assert solution("0P") == False