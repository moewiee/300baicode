class Solution:
    def minimumOperations(self, nums: list) -> int:
        nums = set(nums)
        return len(nums) - 1 if 0 in nums else len(nums)