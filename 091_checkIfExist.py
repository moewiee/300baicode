class Solution:
    def checkIfExist(self, arr: list) -> bool:
        d = set()
        for n in arr:
            if n*2 in d or n/2 in d:
                return True            
            d.add(n)
        return False