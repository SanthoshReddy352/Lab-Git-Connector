"""
Valid Anagram · Easy · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-25 · 6 min · accepted 133/133
"""

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = collections.Counter(s)
        for i in t:
            if i in c1:
                c1[i] -= 1
            else:
                return False 
        if max(c1.values()) == 0:
            return True
        return False
