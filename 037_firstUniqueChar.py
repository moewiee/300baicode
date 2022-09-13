class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, ch in enumerate(s):
            if ch in d.keys():
                d[ch] = 1000000
            else:
                d[ch] = i
        
        min_idx = min(d.values())
        
        return min_idx if min_idx != 1000000 else -1