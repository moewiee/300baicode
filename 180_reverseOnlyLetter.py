from string import ascii_lowercase, ascii_uppercase

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = set(ascii_lowercase + ascii_uppercase)
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and s[i] not in letters:
                i += 1
            while j >= 0 and s[j] not in letters:
                j -= 1
            if i < len(s) and j >=0 and i < j:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
            i += 1
            j -= 1
        
        return ''.join(s)