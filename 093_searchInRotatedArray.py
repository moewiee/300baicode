class Solution:
    def findPivot(self, nums):
        low = 0
        high = len(nums) - 1
        mid = int((high+low)/2)
        visited = set()
        
        while mid not in visited:
            if nums[mid] > nums[0]:
                low = mid
            else:
                high = mid
            visited.add(mid)
            mid = int((high+low)/2)

        return mid
    
    def binSearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
    
    def search(self, nums: list, target: int) -> int:
        if nums[0] > nums[-1]:
            pivot = self.findPivot(nums)
            if target >= nums[0]:
                return self.binSearch(nums[:pivot+1], target)
            else:
                idx = self.binSearch(nums[pivot+1:], target)
                if idx == -1:
                    return idx
                return idx + pivot + 1
        else:
            return self.binSearch(nums, target)
            