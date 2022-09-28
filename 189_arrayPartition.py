class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        minSum = 0
        for i in range(0, len(nums), 2): minSum += nums[i]
        return minSum