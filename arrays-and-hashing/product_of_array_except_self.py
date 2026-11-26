"""
Product of Array Except Self · Medium · Arrays & hashing
Patterns: Prefix sums & difference arrays
Solved in the Lab on 2026-11-26 · 30 min · accepted 134/134
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [0]*len(nums)
        pos = [0]*len(nums)
        pos[-1] = nums[-1]
        pre[0]=(nums[0])
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            pos[i] = pos[i+1]*nums[i]
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i == len(nums) - 1:
                res[i] = pre[i-1]
            elif i != 0:
                res[i] = pre[i-1]*pos[i+1]
            else:
                res[i] = pos[i+1]
        return res
