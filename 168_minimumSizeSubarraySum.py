class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        prefixSum = [0]
        for n in nums: prefixSum.append(prefixSum[-1] + n)        
        if prefixSum[-1] < target: return 0
        elif prefixSum[-1] == target: return len(nums)
            
        i, j, shortest = 0, 1, 200000
        
        while j < len(prefixSum):
            if prefixSum[j] - prefixSum[i] < target: j += 1
            else:
                if j - i < shortest: shortest = j - i
                i += 1
        
        return shortest