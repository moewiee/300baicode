class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int(high / 2 + low / 2 + 0.5)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low