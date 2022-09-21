List = list 

class Solution:
    def findPivot(self, nums):
        if nums[0] <= nums[-1]: # not rotated lol
            return -1
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
    
    def findMin(self, nums: List[int]) -> int:
        return nums[self.findPivot(nums) + 1]