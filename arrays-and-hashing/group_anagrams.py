"""
Group Anagrams · Medium · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-25 · 1 min · accepted 132/132
"""

from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # groups = defaultdict(list)

        # for word in strs:
        #     sign = frozenset(Counter(word).items())
        #     groups[sign].append(word)

        # return sorted(list(groups.values()))
        groups = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
