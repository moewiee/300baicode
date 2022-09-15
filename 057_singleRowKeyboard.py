class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {ch:i for i, ch in enumerate(keyboard)}
        ret = d[word[0]]
        for i in range(1, len(word)):
            ret += abs(d[word[i]] - d[word[i-1]])
        return ret