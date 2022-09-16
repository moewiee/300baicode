class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        d_ch = {}
        d_w = {}
        for ch, w in zip(pattern, s):
            if ch not in d_ch:
                d_ch[ch] = w
            else:
                if d_ch[ch] != w: return False
            if w not in d_w:
                d_w[w] = ch
            else:
                if d_w[w] != ch: return False
        return True