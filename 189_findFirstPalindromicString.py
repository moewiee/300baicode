class Solution:
    def isPal(self, word):
        i = 0
        j = len(word) - 1
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True
    
    def firstPalindrome(self, words: list) -> str:
        for w in words:
            if self.isPal(w): return w
        return ''
        