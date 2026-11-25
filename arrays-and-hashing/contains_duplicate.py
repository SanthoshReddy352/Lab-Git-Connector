"""
Contains Duplicate · Easy · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-25 · 4 min · accepted 133/133
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
