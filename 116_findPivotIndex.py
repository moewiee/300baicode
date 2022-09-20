class Solution:
    def pivotIndex(self, nums: list) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if totalSum - 2 * leftSum - nums[i] == 0:
                return i            
            leftSum += nums[i]
        return -1