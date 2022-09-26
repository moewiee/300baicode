class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        i = 0
        j = 0
        longest = 1
        while j < len(nums) - 1:
            if nums[j + 1] > nums[j]:
                j += 1
                longest = max(longest, j - i + 1)
            else:
                j += 1
                i = j
        return longest