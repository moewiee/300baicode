class Solution:
    def chalkReplacer(self, chalk: list, k: int) -> int:
        k = k % sum(chalk)
        for i, n in enumerate(chalk):
            k -= n
            if k < 0:
                return i