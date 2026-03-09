import pytest
from contains_duplicate_1 import Solution as Solution1
from contains_duplicate_2 import Solution as Solution2
from contains_duplicate_3 import Solution as Solution3

solutions = [
    Solution1().containsDuplicate,
    Solution2().containsDuplicate,
    Solution3().containsDuplicate,
]

@pytest.mark.parametrize("solution", solutions)
class TestContainsDuplicate:

    def test_with_duplicate(self, solution):
        assert solution([1, 2, 3, 3]) == True

    def test_without_duplicate(self, solution):
        assert solution([1, 2, 3, 4]) == False

    def test_single_element(self, solution):
        assert solution([1]) == False

    def test_all_duplicates(self, solution):
        assert solution([2, 2, 2, 2]) == True

    def test_empty_array(self, solution):
        assert solution([]) == False

    def test_large_input_no_duplicate(self, solution):
        assert solution(list(range(1000))) == False

    def test_large_input_with_duplicate(self, solution):
        nums = list(range(999)) + [0]
        assert solution(nums) == True
