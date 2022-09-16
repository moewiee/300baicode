class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftToRight = []
        for i, n in enumerate(nums):
            if n is 0:
                leftToRight.append(i)
            else:
                if leftToRight:
                    nums[leftToRight[0]] = n
                    nums[i] = 0
                    leftToRight.append(i)
                    leftToRight.pop(0)