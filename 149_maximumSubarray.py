class Solution(object):
    def maxSubArray(self, nums):
        maxEndingHere = 0
        maxEndingSoFar = -2*10**4
        
        for n in nums:
            maxEndingHere += n
            maxEndingSoFar = max(maxEndingHere, maxEndingSoFar)
            maxEndingHere = max(maxEndingHere, 0)
            
        return maxEndingSoFar