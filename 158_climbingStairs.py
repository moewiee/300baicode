class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [1,2]
        for i in range(2, n): climb.append(climb[-1] + climb[-2])
        return climb[-1] if n >= 3 else climb[n-1]