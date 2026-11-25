"""
Group Anagrams · Medium · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-25 · 8 min · accepted 132/132
"""

from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            sign = frozenset(Counter(word).items())
            groups[sign].append(word)

        return sorted(list(groups.values()))
