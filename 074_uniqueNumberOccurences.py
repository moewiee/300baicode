class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        d = {}
        for n in arr:
            d[n] = d[n] + 1 if n in d.keys() else 1
        return len(set(d.values())) == len(list(d.values()))