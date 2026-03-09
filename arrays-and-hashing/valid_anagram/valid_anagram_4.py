class Solution:
    # 1 Hash map approach.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            # We could have skipped this step and just 
            # checked if all counts are zero at the end, 
            # but this way we can potentially return False earlier.
            if count[char] == 0:
                del count[char]
        return len(count) == 0
# Time complexity: O(n)
# Space complexity: O(k) -  k =  number of unique chars in the strings
