class Solution:
    def search(self, nums: list, target: int) -> int:      
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((high+low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
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
        
    
    def searchLast(self, nums:list, target:int) -> int:
        low = 0
        high = len(nums) - 1
        
        while high >= low:
            mid = int((high+low)/2)
            
            if nums[mid] == target:
                if mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                    low = mid + 1
                else:
                    return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    
    def searchRange(self, nums:list, target:int) -> list:
        # check if target present
        targetIdx = self.search(nums, target)
        if targetIdx == -1:
            return [-1, -1]

        # target present
        return [self.searchFirst(nums[:targetIdx+1], target), targetIdx + self.searchLast(nums[targetIdx:], target)]
        