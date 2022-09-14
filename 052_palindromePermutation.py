class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = [0] * 26
        for ch in s:
            chars[ord(ch) - 97] = 1 - chars[ord(ch) - 97]
        return True if sum(chars) < 2 else False