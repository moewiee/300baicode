class Solution:
    def sumOfUnique(self, nums: list) -> int:
        d = {}
        for n in nums:
            d[n] = d[n] + 1 if n in d else 1
        return sum([n for n in d if d[n] == 1])