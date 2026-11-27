"""
Valid Sudoku · Medium · Arrays & hashing
Patterns: Hash maps & sets
Solved in the Lab on 2026-11-27 · 1 min · accepted 161/161
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        r = {}
        c = {}
        b = {}

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                num = int(board[i][j])
                box = (i // 3) * 3 + (j // 3)

                if i not in r:
                    r[i] = set()

                if j not in c:
                    c[j] = set()

                if box not in b:
                    b[box] = set()

                if num in r[i] or num in c[j] or num in b[box]:
                    return False

                r[i].add(num)
                c[j].add(num)
                b[box].add(num)

        return True
