class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash map two pass approach.
        num_map = {}
        for i, n in enumerate(nums):
            num_map[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        return []
        
# Time complexity: O(n)
# Space complexity: O(n)