class Solution:
    def repeatedNTimes(self, nums: list) -> int:
        s = set()
        for n in nums:
            if n in s: return n
            s.add(n)