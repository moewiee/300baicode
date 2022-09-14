class Solution:
    def numIdenticalPairs(self, nums: líst) -> int:
        ret = 0
        d = {}
        for i, n in enumerate(nums):
            if n not in d.keys():
                d[n] = [i]
            else:
                d[n] += [i]
        for n in d.keys():
            if len(d[n]) >= 2:
                ret += len(d[n]) * (len(d[n]) - 1) / 2
                
        return int(ret)