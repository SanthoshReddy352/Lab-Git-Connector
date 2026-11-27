"""
Valid Sudoku · Medium · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-27 · 1 min · accepted 161/161
"""

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                ri = int(board[i][j])
                if ri in c[j]:
                    return False
                elif ri in r[i]:
                    return False
                elif ri in b[(i//3)*3+(j//3)]:
                    return False
                else:
                    c[j].add(ri) 
                    r[i].add(ri)
                    b[(i//3)*3+(j//3)].add(ri)
        return True
