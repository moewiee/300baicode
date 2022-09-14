class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        max_degree = 0
        subArrayIndex = [0, 50000]
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [[i], 1]
            else:
                d[n][0].append(i)
                d[n][1] += 1
                if d[n][1] >= max_degree:
                    if max_degree == d[n][1]:
                        if subArrayIndex[1] - subArrayIndex[0] > d[n][0][-1] - d[n][0][0]:
                            subArrayIndex = [d[n][0][0], d[n][0][-1]]
                    else:
                        subArrayIndex = [d[n][0][0], d[n][0][-1]]
                    max_degree = d[n][1]
        
        if max_degree >= 2:
            return - subArrayIndex[0] + subArrayIndex[1] + 1
        else:
            return 1