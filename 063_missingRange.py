class Solution:
    def findMissingRanges(self, nums: list, lower: int, upper: int) -> list:
        nums = [lower-1] + nums + [upper+1]
        ret = []
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 2:
                ret += [str(int((nums[i+1] + nums[i]) / 2))]
            elif nums[i+1] - nums[i] > 2:
                ret += [f'{nums[i] + 1}->{nums[i+1] - 1}']
                
        return ret