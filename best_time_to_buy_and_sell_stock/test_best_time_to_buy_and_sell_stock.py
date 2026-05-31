import pytest
from best_time_to_buy_and_sell_stock import Solution

solution = Solution().maxProfit

class TestMaxProfit:

    def test_leetcode_example_1(self):
        assert solution([7, 1, 5, 3, 6, 4]) == 5

    def test_leetcode_example_2(self):
        assert solution([7, 6, 4, 3, 1]) == 0

    def test_single_element(self):
        assert solution([5]) == 0

    def test_two_elements_profit(self):
        assert solution([1, 5]) == 4

    def test_two_elements_no_profit(self):
        assert solution([5, 1]) == 0

    def test_all_same(self):
        assert solution([3, 3, 3, 3]) == 0

    def test_buy_at_end(self):
        assert solution([10, 9, 8, 7, 6, 1]) == 0

    def test_max_at_end(self):
        assert solution([1, 2, 3, 4, 5]) == 4