class Solution:
    def arithmeticTriplets(self, nums: list, diff: int) -> int:
        s = set()
        ret = 0
        for n in nums:
            if n-diff in s and n-diff-diff in s:
                ret += 1
            s.add(n)
        return ret