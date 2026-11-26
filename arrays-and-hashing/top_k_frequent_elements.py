"""
Top K Frequent Elements · Medium · Arrays & hashing
Patterns: Hash maps & sets, Top-K & k-way merge
Solved in the Lab on 2026-11-26 · 6 min · accepted 131/131
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return [nums[0]]
        c = Counter(nums)
        return sorted(c,key=c.get,reverse=True)[:k]
