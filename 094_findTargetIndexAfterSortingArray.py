class Solution:
    def targetIndices(self, nums: list, target: int) -> list:
        target_count = 0
        smaller_count = 0
        for n in nums:
            if n == target:
                target_count += 1
            elif n < target:
                smaller_count += 1
        return [smaller_count + i for i in range(0, target_count)]