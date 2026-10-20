"""
Mean squared error · Easy · Losses
Patterns: Fitting a line
Solved in the Lab on 2026-10-20 · 1 min · accepted 3/3
"""

class Solution:
    def mse(self, pred: list[float], target: list[float]) -> float:
        return sum((p - t) ** 2 for p, t in zip(pred, target)) / len(pred)
