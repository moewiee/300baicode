class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        e,i,o,a,u = 0,0,0,0,0
        d = {'00000': 0}
        longest = 0
        for idx, ch in enumerate(s):
            if ch == 'e':
                e = 1-e
            elif ch == 'i':
                i = 1-i
            elif ch == 'o':
                o = 1-o
            elif ch == 'a':
                a = 1-a
            elif ch == 'u':
                u = 1-u
            keystring = str([e,i,o,a,u])[1:-1:3]
            if keystring in d:
                longest = max(longest, idx - d[keystring] + 1)
            else:
                d[keystring] = idx + 1
        return longest