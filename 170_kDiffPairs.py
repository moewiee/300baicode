from collections import Counter

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        counter = Counter(nums)
        count = 0
        for n in counter:
            if k > 0 and n + k in counter:
                count += 1
            elif k == 0 and counter[n] > 1:
                count += 1
        return count