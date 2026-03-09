from collections import Counter
class Solution:
    # Pythonic approach with Counter.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
# Time complexity: O(n) - creating counters
# Space complexity: O(k) -  k =  number of unique chars in the strings
