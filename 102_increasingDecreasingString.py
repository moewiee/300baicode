class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d[ch] + 1 if ch in d else 1
        i = len(s)
        increasing = 1
        ret = ''
        while i:
            if increasing:
                for ch in sorted(d):
                    if d[ch] > 0:
                        ret += ch
                        d[ch] -= 1
                        i -= 1
            else:
                for ch in sorted(d)[::-1]:
                    if d[ch] > 0:
                        ret += ch
                        d[ch] -= 1
                        i -= 1
            increasing = 1 - increasing
            
        return ret