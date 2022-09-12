class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        out1 = []
        out2 = []
        for ch1 in s:
            if ch1 != '#':
                out1.append(ch1)
            else:
                if out1:
                    out1.pop()
        for ch2 in t:                
            if ch2 != '#':
                out2.append(ch2)
            else:
                if out2:
                    out2.pop()
                
        print(out1, out2)
        return out1 == out2
                