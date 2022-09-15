class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        invalid = {'2','3','4','5','7'}
        valid = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        flag = 0
        i = 0
        j = len(n) - 1
        while i <= j:
            if n[i] in invalid:
                return False
            if n[j] in invalid:
                return False
            if valid[n[i]] != n[j]:
                flag = 1
            i += 1
            j -= 1
        return flag