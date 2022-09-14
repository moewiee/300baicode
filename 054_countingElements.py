class Solution:
    def countElements(self, arr: list) -> int:
        ok = set()
        ret = 0
        for n in arr:
            ok.add(n-1)
        for n in arr:
            if n in ok: ret += 1
                
        return ret