"""
Contains Duplicate · Easy · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-10-19 · 21 min · accepted 133/133
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
