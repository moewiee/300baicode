class Solution:
    def numSubarraysWithSum(self, nums: list, goal: int) -> int:
        prefixSum = []
        current = 0
        d = {0:1}
        count = 0
        for n in nums:
            current += n
            prefixSum.append(current)
            if current - goal in d:
                count += d[current - goal]
            if current in d:
                d[current] += 1
            else:
                d[current] = 1
        
        return count