class Solution:
    def diStringMatch(self, s: str) -> list:
        ret, retMin, retMax = [0], 0, 0
        for ch in s:
            if ch == 'I':
                ret.append(retMax + 1)
                retMax += 1
            else:
                ret.append(retMin - 1)
                retMin -= 1
        for i in range(len(ret)): ret[i] -= retMin
        return ret