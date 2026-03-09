class Solution:
    # Sorting approach.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # before sorting, if lengths are different, they can't be anagrams)
            return False
        return sorted(s) == sorted(t)
# Time complexity: O(n log n) - sorting the strings
# Space complexity: O(n) - sorting creates new lists of characters
