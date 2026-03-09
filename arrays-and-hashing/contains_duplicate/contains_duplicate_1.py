class Solution:
    # Pythonic approach.
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums) # != or <
# Time complexity: O(n)
# Space complexity: O(n)
