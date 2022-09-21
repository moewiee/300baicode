List = list

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            while prices[l] > prices[r]:
                if r == len(prices) - 1: 
                    return maxProfit
                l = r
                r += 1
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        
        return maxProfit