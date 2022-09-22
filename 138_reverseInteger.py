class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10: 
            return x  
        signed = x < 0
        x = -x if signed else x
        
        limit = [2,1,4,7,4,8,3,6,4,7]
        
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = int((x - digits[-1]) / 10)
        
        i = 0
        while digits[i] == 0:
            i += 1
        digits = digits[i:]
        
        if len(digits) == 10:
            for i in range(10):
                if digits[i] > limit[i]:
                    return 0
                elif digits[i] < limit[i]:
                    break
        
        x = 0
        for i in range(len(digits)):
            x += digits[i] * 10**(len(digits) - i - 1)
            
        return -x if signed else x