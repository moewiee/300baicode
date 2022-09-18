class Solution:
    def mySqrt(self, x: int) -> int:
        visited = set()
        low = 0
        high = x
        mid = int(x/2)
        while mid not in visited:
            visited.add(mid)
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                high = mid - 1
                mid = int((high + low) / 2)
            else:
                low = mid + 1
                mid = int((high + low) / 2)
        
        return mid