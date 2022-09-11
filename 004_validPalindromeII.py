class Solution:
    def altPalindrome(self, s:str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if self.altPalindrome(s[i+1:j+1]):
                    return True
                else:
                    return self.altPalindrome(s[i:j])
        return True
