class Solution:
    def rob(self, nums: list, ret=None) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        if ret == None:
            ret = {}
            
        key = str(nums)
        if key not in ret:
            ret[key] = max(nums[0] + self.rob(nums[2:], ret), nums[1] + self.rob(nums[3:], ret))
            
        return ret[key]