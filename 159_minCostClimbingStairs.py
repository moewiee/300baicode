class Solution:
    def minCostClimbingStairs(self, cost: list, ret=None) -> int:
        if len(cost) == 1: return 0
        if len(cost) == 2: return min(cost)
        if ret == None: ret = {}
        
        key = str(cost)
        if key not in ret: ret[key] = min(cost[0] + self.minCostClimbingStairs(cost[1:], ret), cost[1] + self.minCostClimbingStairs(cost[2:], ret))
        return ret[key]