class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        for ch in s:
            s_dict[ch] = s_dict[ch] + 1 if ch in s_dict else 1
        for ch in t:
            if ch in s_dict:
                s_dict[ch] -= 1
                if s_dict[ch] < 0:
                    return ch
            else:
                return ch