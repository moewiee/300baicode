class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = str(num)
        invalid = {'2','3','4','5','7'}
        valid = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        i = 0
        j = len(n) - 1
        while i <= j:
            if n[i] in invalid:
                return False
            if n[j] in invalid:
                return False
            if valid[n[i]] != n[j]:
                return False
            i += 1
            j -= 1
        return True