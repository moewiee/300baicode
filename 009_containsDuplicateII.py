class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d.keys():
                d[n].append(i)
                if d[n][-1] - d[n][-2] <= k:
                    return True
            else:
                d[n] = [i]
                
        return False