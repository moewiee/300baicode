class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        d = {}
        for i, gs in enumerate(groupSizes):
            d[gs] = d[gs] + [i] if gs in d else [i]
        ret = []
        for size in d:
            i = 0
            while i < len(d[size]):
                ret.append(d[size][i:i+size])
                i += size
        return ret