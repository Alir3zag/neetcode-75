from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """Two pointers — O(n) time, O(1) space."""
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area