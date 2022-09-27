class Solution:
    def subRob(self, nums, ret=None):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        if ret is None:
            ret = {}
        
        key = str(nums)
        if key not in ret:
            ret[key] = max(nums[0] + self.subRob(nums[2:], ret), nums[1] + self.subRob(nums[3:], ret))
            
        return ret[key]
    
    def rob(self, nums: list) -> int:
        if len(nums) == 1: return nums[0]
        caseRobFirst = self.subRob(nums[:-1])
        caseRobSecond = self.subRob(nums[1:])
        
        return max(caseRobFirst, caseRobSecond)