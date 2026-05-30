from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            group = [0] * 26
            for char in word:
                group[ord(char) - ord('a')] += 1
            groups[tuple(group)] = groups.get(tuple(group), []) + [word]
        return list(groups.values())
