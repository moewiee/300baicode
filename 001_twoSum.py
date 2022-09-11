class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ud = dict()
        ret = []
        for i, n in enumerate(nums):
            if str(n) not in ud.keys():
                ud[str(n)] = [i]
            else:
                ud[str(n)].append(i)
        for n in nums:
            if str(target - n) in ud.keys():
                if n == (target - n):
                    if len(ud[str(n)]) == 2:
                        return [ud[str(n)][0], ud[str(n)][1]]
                else:
                    return [ud[str(n)][0], ud[str(target - n)][0]]