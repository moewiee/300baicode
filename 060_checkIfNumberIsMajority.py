class Solution:
    def first(self, arr, low, high, x, n):
        if(high >= low):
            mid = low + (high - low) // 2
            if((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
                return mid
            elif(x > arr[mid]):
                return self.first(arr, (mid + 1), high, x, n)
            else:
                return self.first(arr, low, (mid - 1), x, n)

        return -1

    def last(self, arr, low, high, x, n):
        if (high >= low):
            mid = low + (high - low) // 2
            if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
                return mid
            elif (x < arr[mid]):
                return self.last(arr, low, (mid - 1), x, n)
            else:
                return self.last(arr, (mid + 1), high, x, n)

        return -1
    
    def isMajorityElement(self, nums: list, target: int) -> bool:
        first = self.first(nums, 0, len(nums) - 1, target, len(nums))
        if first != -1:
            last = self.last(nums, 0, len(nums) - 1, target, len(nums))
            return (last-first+1) * 2 > len(nums)
        return False