class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        d = {}
        s = set()
        for n in nums:
            d[n] = d[n] + 1 if n in d else 1
        ret = 0
        for n in d:
            if n + k in d:
                ret += d[n] * d[n+k]
        return ret