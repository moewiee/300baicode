class Solution:
    def canBeEqual(self, target: list, arr: list) -> bool:
        d = {}
        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for n in target:
            if n not in d or d[n] == 0:
                return False
            d[n] -= 1
        
        return True