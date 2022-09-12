class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        sq = []
        
        while x >= 1:
            sq.append(x % 10)
            x = int(x/10)
        
        while len(sq) >= 2:
            if sq.pop() != sq.pop(0):
                return False
        
        return True
            