class Solution:
    # Sorting approach.
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
# Time complexity: O(n log n)
# Space complexity: O(1)
