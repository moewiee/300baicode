class Solution:
    def maxSubArrayLen(self, nums: list, k: int) -> int:
        sumDict = {}
        running_sum = 0
        longest = 0
        
        for i, n in enumerate(nums):
            running_sum += n
            if running_sum == k:
                longest = i+1
            if running_sum - k in sumDict:
                longest = max(longest, i - sumDict[running_sum - k])
            if running_sum not in sumDict:
                sumDict[running_sum] = i
    
        return longest