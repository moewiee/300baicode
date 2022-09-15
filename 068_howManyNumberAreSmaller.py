class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        d = [0] * 101
        for n in nums:
            d[n] += 1
        smaller_count = [0] * 101
        running_sum = 0
        for i in range(1, 101):
            running_sum += d[i-1]
            smaller_count[i] = running_sum
            
        return [smaller_count[n] for n in nums]