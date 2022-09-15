class Solution:
    def twoSumLessThanK(self, nums: list, k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        ret = 0
        while i < j:
            if nums[i] + nums[j] < k:
                if nums[i] + nums[j] > ret:
                    ret = nums[i] + nums[j]
                i += 1
            else:
                j -= 1
        return ret if ret else -1