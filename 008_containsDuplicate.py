class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = {}
        for n in nums:
            if n in d.keys():
                return True
            else:
                d[n] = 0
        
        return False