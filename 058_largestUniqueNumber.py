class Solution:
    def largestUniqueNumber(self, nums: list) -> int:
        appear_once = set()
        appear_more_than_once = set()
        
        for n in nums:
            if n not in appear_more_than_once:
                if n not in appear_once:
                    appear_once.add(n)
                else:
                    appear_once.remove(n)
                    appear_more_than_once.add(n)
        
        return max(list(appear_once)) if appear_once else -1