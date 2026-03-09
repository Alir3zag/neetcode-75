class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash map one pass approach. last one has a redundant loop to 
        # build the hash map first, we can do it in one pass.
        num_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map:
                return [num_map[complement], i]
            num_map[n] = i
        return []
        
# Time complexity: O(n)
# Space complexity: O(n)