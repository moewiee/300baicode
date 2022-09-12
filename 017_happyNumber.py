class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)    
            digit = []
            while n > 0:
                digit.append(n % 10)
                n = int(n/10)
            
            n = sum([f**2 for f in digit])
            if n == 1:
                return True
            if n in s:
                return False