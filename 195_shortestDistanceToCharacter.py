class Solution:
    def shortestToChar(self, s: str, c: str) -> list:
        cIdx = [-100000]
        for i, ch in enumerate(s):
            if ch == c: cIdx.append(i)
        cIdx.append(100000)
        cPtr = 1
        ret = []
        for i, ch in enumerate(s):
            if i >= cIdx[cPtr]: cPtr += 1
            ret.append(min(i - cIdx[cPtr - 1], cIdx[cPtr] - i))
            
        return ret