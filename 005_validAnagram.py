class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for ch in s:
            if ch in s_dict.keys():
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
                
        for ch in t:
            if ch not in s_dict.keys():
                return False
            else:
                if s_dict[ch] == 0:
                    return False
                else:
                    s_dict[ch] -= 1        
        if len(s) != len(t):
            return False
        return True