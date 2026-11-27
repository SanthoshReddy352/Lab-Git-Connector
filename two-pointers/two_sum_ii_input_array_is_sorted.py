"""
Two Sum II (sorted input) · Medium · Two pointers
Patterns: Two pointers
Solved in the Lab on 2026-11-27 · 2 min · accepted 134/134
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0,len(numbers)-1
        while l < r:
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []
