"""
Longest Consecutive Sequence · Medium · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-28 · 10 min · accepted 133/133
"""

from collections import Counter
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        mlcs = 0
        for i in nums:
            if i-1 not in nums:
                j = i 
                lcs = 1
                while j+1 in nums:
                        lcs += 1
                        j += 1
                mlcs = max(lcs, mlcs)
        return mlcs
