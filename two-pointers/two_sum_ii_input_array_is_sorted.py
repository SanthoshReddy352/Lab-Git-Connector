"""
Two Sum II (sorted input) · Medium · Two pointers
Patterns: Two pointers
Solved in the Lab on 2026-11-26 · 6 min · accepted 134/134
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i,j in enumerate(numbers):
            c = target - j
            if c in seen:
                return [seen[c]+1,i+1]
            seen[j] = i
