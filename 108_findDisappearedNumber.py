class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        length = len(nums)
        nums = set(nums)
        return [i for i in range(1, length + 1) if i not in nums]