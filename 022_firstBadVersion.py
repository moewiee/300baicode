# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n: int) -> bool:
    return n > 0

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            pivot = int((low + high) / 2)
            if isBadVersion(pivot): # move left
                if isBadVersion(pivot - 1):
                    high = pivot - 1
                else:
                    return pivot
            else: # move right
                low = pivot + 1
            