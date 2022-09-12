class Solution:
    def missingNumber(self, nums: list) -> int:
        full_sum = len(nums) * (len(nums) + 1) / 2
        missed_sum = sum(nums)
        
        return int(full_sum - missed_sum)