class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Sorted two pointer approach. We can sort it and 
        # keep track of the original indices.
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1]) # sort by value, but still keep original index
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if current_sum == target:
                return [min(sorted_nums[left][0], sorted_nums[right][0]), max(sorted_nums[left][0], sorted_nums[right][0])]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

# Time complexity: O(n log n)
# Space complexity: O(n) - we create a new list of sorted tuples
