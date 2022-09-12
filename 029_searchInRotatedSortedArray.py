binary_search = __import__('019_binarySearch')

class Solution:
    def __init__(self):
        self.binary_searcher = binary_search.Solution()

    def remake(self, nums):
        if len(nums) < 2:
            return 0, nums
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 1, nums[::-1]
            else:
                return 0, nums
        
        pivot = -1
        for i in range(1, len(nums), 1):
            if nums[i] < nums[i-1]:
                pivot = i
        if pivot != -1:
            return pivot, nums[-(len(nums)-pivot):] + nums[:pivot]
        else:
            return 0, nums

    def search(self, nums: list, target: int) -> int:
        pivot, nums = self.remake(nums)
        idx = self.binary_searcher.search(nums, target)

        if idx != -1:
            tail_nums = len(nums) - pivot
            if idx < tail_nums:
                return idx + pivot
            else:
                return idx - tail_nums
        else:
            return -1


        

if __name__ == '__main__':
    s = Solution()
    assert s.search([4,5,6,7,0,1,2], 1) == 5
    assert s.search([3,5,1], 1) == 2
    assert s.search([1,3,5], 1) == 0

    print('TEST PASSED!')