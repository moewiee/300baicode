class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        for _ in range(n - 2):
            dp.append(dp[-1] + dp[-2])
            
        return dp[n-1]
            