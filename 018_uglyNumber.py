class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 == 0:
                n = int(n/2)
            elif n % 3 == 0:
                n = int(n/3)
            elif n % 5 == 0:
                n = int(n/5)
            else:
                return False
        if n == 1:
            return True
        return False