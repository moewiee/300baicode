class Solution:
    def largestSubarray(self, nums: list, k: int) -> list:
        maxElement = 0
        maxIndex = 0
        for i in range(len(nums[:len(nums)-k+1])): 
            if nums[i] > maxElement:
                maxElement = nums[i]
                maxIndex = i
        return nums[maxIndex:maxIndex+k]