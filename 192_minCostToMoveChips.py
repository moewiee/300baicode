class Solution:
    def minCostToMoveChips(self, position: list) -> int:
        chipsOdd = 0
        chipsEven = 0
        for p in position:
            if p % 2: chipsOdd += 1
            else: chipsEven += 1
        return min(chipsOdd, chipsEven)