"""
Contains Duplicate · Easy · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-10-19 · 5 min · accepted 133/133
"""

# contains-duplicate: write your solution below. Running it arrives with the Workbench (P2).

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
