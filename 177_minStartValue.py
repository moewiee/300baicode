class Solution:
    def minStartValue(self, nums: list) -> int:
        prefixSum = 0
        minPrefixSum = 1000
        
        for n in nums:
            prefixSum += n
            minPrefixSum = min(prefixSum, minPrefixSum)
            
        return max(1 - minPrefixSum, 1)