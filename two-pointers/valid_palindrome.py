"""
Valid Palindrome · Easy · Two pointers
Patterns: Two pointers
Solved in the Lab on 2026-11-28 · 5 min · accepted 135/135
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        i, j = 0, len(s)-1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
