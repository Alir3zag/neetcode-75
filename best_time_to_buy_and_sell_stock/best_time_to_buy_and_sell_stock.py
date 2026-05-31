from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxpro = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxpro = max(maxpro, prices[r] - prices[l])
        return maxpro