class Solution:
    def search(self, num, target):
        low = 0
        high = len(num) - 1
        while low <= high:
            mid = int(int(high+low)/2)
            if num[mid] == target:
                return mid
            elif num[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    def searchFirst(self, nums:list, target:int) -> int:
        low = 0
        high = len(nums) - 1
        
        while high >= low:
            mid = int((high+low)/2)
            
            if nums[mid] == target:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    high = mid - 1
                else:
                    return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
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
    
    def specialArray(self, nums: list) -> int:
        length = len(nums)
        nums.sort()
        
        for target in range(len(nums) + 1):
            searchIdx = self.search(nums, target)
            if searchIdx == -1: # target not in nums, find insert position -> n greater = len(nums) - insertIdx
                if len(nums) - self.searchInsert(nums, target) == target: return target
            else: # target in nums, find first occurent -> n greaterEqual = len(nums) - firstIdx
                if len(nums) - self.searchFirst(nums, target) == target: return target
        
        return -1