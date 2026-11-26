"""
Encode and Decode Strings · Medium · Arrays & hashing
Patterns: Arrays & strings
Solved in the Lab on 2026-11-26 · 6 min · accepted 132/132
"""

class Solution:
    def encode(self, strs: list[str]) -> str:
        chunks = []
        for s in strs:
            chunks.append(f"{len(s)}#{s}")
        return "".join(chunks)
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        n = len(s)
        while i<n:
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j+1
            end = start + length
            res.append(s[start:end])
            i = end
        return res
