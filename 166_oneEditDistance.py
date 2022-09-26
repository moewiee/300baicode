class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) >= 2: return False
        if s == t: return False
        
        edit = 0
        
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    if not edit:
                        edit = 1
                    else:
                        return False
        else:
            if len(t) > len(s):
                tmp = s
                s = t
                t = tmp
            j = 0
            for i in range(len(t)):
                if s[j] != t[i]:
                    j += 1
                    if not edit:
                        edit = 1
                        if s[j] != t[i]: return False
                    else:
                        return False
                j += 1
                
        return True