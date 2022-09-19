class Solution:
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
        
        return -1
    
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
    
    def answerQueries(self, nums: list, queries: list) -> list:
        nums.sort()
        sum_array = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            sum_array.append(running_sum)
        
        ret = []
        for q in queries:
            idx = self.searchLast(sum_array, q)
            if idx != -1:
                ret.append(idx + 1)
            else:
                ret.append(self.searchInsert(sum_array, q))
                
        return ret