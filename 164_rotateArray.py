class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums += [0] * (l - k)
        i = 0
        j = l
        while j < len(nums):
            nums[j] = nums[i]
            i += 1
            j += 1
        
        while len(nums) > l:
            nums.pop(0)