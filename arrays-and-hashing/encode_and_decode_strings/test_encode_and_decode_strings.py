import pytest
from encode_and_decode_strings import Solution

sol = Solution()

class TestEncodeDecodeStrings:

    def test_leetcode_example_1(self):
        strs = ["neet", "code", "love", "you"]
        assert sol.decode(sol.encode(strs)) == strs

    def test_leetcode_example_2(self):
        strs = ["we", "say", ":", "yes"]
        assert sol.decode(sol.encode(strs)) == strs

    def test_empty_list(self):
        assert sol.decode(sol.encode([])) == []

    def test_empty_string(self):
        assert sol.decode(sol.encode([""])) == [""]

    def test_multiple_empty_strings(self):
        assert sol.decode(sol.encode(["", "", ""])) == ["", "", ""]

    def test_string_with_hash(self):
        assert sol.decode(sol.encode(["he#llo", "wor#ld"])) == ["he#llo", "wor#ld"]

    def test_string_with_numbers(self):
        assert sol.decode(sol.encode(["123", "456"])) == ["123", "456"]

    def test_single_char(self):
        assert sol.decode(sol.encode(["a"])) == ["a"]

    def test_special_characters(self):
        assert sol.decode(sol.encode(["!@#", "$%^", "&*("])) == ["!@#", "$%^", "&*("]

    def test_single_long_string(self):
        strs = ["a" * 100]
        assert sol.decode(sol.encode(strs)) == strs