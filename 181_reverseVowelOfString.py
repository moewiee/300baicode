class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        ret = []
        while i < j:
            while i < j and i < len(s) and s[i] not in tuple('aeiouAEIOU'): i += 1
            while j > i and j >= 0 and s[j] not in tuple('aeiouAEIOU'): j -= 1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        
        return ''.join(s)