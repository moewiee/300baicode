class Solution:
    def findErrorNums(self, nums: list) -> list:
        totalSum = (len(nums) * (len(nums) + 1)) / 2
        thisSum = 0
        visited = set()
        ret = []
        
        for n in nums:
            if n in visited: 
                ret.append(n)
            else:
                thisSum += n
                visited.add(n)
        
        ret.append(int(totalSum - thisSum))
        return ret