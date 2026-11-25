"""
Two Sum · Easy · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-25 · 19 min · accepted 135/135
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            s = target - nums[i]
            if s in seen:
                return [seen[s],i]
            seen[nums[i]] = i
