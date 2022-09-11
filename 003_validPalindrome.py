import re
valid_chars = tuple('qwertyuiopasdfghjklzxcvbnm0123456789')

class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp = re.compile('[^a-z^0-9]')
        s = s.lower()
        s = comp.sub('', s)
        i = 0
        j = len(s) - 1
        flag = 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return flag