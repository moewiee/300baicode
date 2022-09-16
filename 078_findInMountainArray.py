# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass
    def length(self) -> int:
        pass

class Solution:
    def __init__(self):
        self.known = {}
        self.apiCallCount = 0
        
    def getVal(self, mountain_arr, idx):
        if idx in self.known.keys():
            return self.known[idx]
        ret = mountain_arr.get(idx)
        self.apiCallCount += 1
        self.known[idx] = ret
        
        return self.known[idx]
        
    
    def findPeak(self, mountain_arr):
        low = 0
        high = mountain_arr.length() - 1
        mid = int((low + high) / 2)
        
        while low <= high:
            if mid and self.getVal(mountain_arr, mid-1) < self.getVal(mountain_arr, mid) and self.getVal(mountain_arr, mid) > self.getVal(mountain_arr, mid+1):
                return mid
            else:
                if mid == 0:
                    return 1
                elif self.getVal(mountain_arr, mid - 1) < self.getVal(mountain_arr, mid):
                    low = mid+1
                    mid = int((low + high) / 2)
                else:
                    high = mid-1
                    mid = int((low + high) / 2)
    
    def searchIncrease(self, mountain_arr, peak, target):
        low = 0
        high = peak
        mid = int((low + high) / 2)
        
        while low <= high:
            if self.getVal(mountain_arr, mid) == target:
                return mid
            elif self.getVal(mountain_arr, mid) < target:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                high = mid - 1
                mid = int((low + high) / 2)
                
        return -1
    
    def searchDecrease(self, mountain_arr, peak, target):
        low = peak
        high = mountain_arr.length() - 1
        mid = int((low + high) / 2)
        
        while low <= high:
            if self.getVal(mountain_arr, mid) == target:
                return mid
            elif self.getVal(mountain_arr, mid) > target:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                high = mid - 1
                mid = int((low + high) / 2)
                
        return -1
        
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peakIdx = self.findPeak(mountain_arr)        
        ret = self.searchIncrease(mountain_arr, peakIdx, target)
        return ret if ret != -1 else self.searchDecrease(mountain_arr, peakIdx, target)
        