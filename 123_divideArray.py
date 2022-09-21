class Solution:
    def divideArray(self, nums: list) -> bool:
        d = [0 for _ in range(501)]
        for n in nums:
            d[n] += 1
        return not any([f % 2 for f in d])