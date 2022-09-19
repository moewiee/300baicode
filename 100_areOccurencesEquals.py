class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:     
        d = {}
        for n in s:
            d[n] = d[n] + 1 if n in d else 1
        return len(set(d.values())) == 1