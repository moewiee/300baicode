class Solution:
    def singleNumber(self, nums: list) -> int:
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] = 2
            else:
                d[n] = 1
        for n in d.keys():
            if d[n] == 1: return n