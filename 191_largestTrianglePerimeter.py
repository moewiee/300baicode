class Solution:
    def isValidTriangle(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a: return False
        return True
    
    def largestPerimeter(self, nums: list) -> int:
        nums.sort()
        i = len(nums) - 3
        while i >= 0 and not self.isValidTriangle(nums[i], nums[i+1], nums[i+2]): i -= 1
        if i == -1: return 0
        else: return nums[i] + nums[i+1] + nums[i+2]