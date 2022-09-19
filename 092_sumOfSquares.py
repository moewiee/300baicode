imp = __import__('085_sqrtX')

class Solution:
    def __init__(self) -> None:
        self.algo = imp.Solution()
    
    def judgeSquareSum(self, c: int) -> bool:
        largestRoot = self.algo.mySqrt(c) # O(logN)
        squares = set()
        for i in range(largestRoot + 1): # O(logN)
            squares.add(i*i)
        for i in squares: # O(logN)
            if c - i in squares:
                return True
        return False
        