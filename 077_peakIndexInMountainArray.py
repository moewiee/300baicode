class Solution:
    def peakIndexInMountainArray(self, arr: list) -> int:
        low = 0
        high = len(arr) - 1
        mid = int((low + high) / 2)
        
        while low <= high:
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            else:
                if mid == 0:
                    return 1
                elif arr[mid-1] < arr[mid]:
                    low = mid+1
                    mid = int((low + high) / 2)
                else:
                    high = mid-1
                    mid = int((low + high) / 2)
