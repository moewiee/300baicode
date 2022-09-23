class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        ret = 0
        for w in text.split():
            if not set(w).intersection(brokenLetters): ret += 1
        return ret