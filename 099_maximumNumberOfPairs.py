class Solution:
    def numberOfPairs(self, nums: list) -> list:
        d = {}
        for n in nums:
            d[n] = d[n] + 1 if n in d else 1
        pairs = 0
        leftovers = 0
        for n in d:
            pairs += int(d[n] / 2)
            leftovers += d[n] % 2
        return [pairs, leftovers]