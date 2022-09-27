class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i, j = 0, 0
        while j < len(word) and word[j] != ch: j += 1
        if j == len(word): return word
        word = list(word)
        while i < j:
            tmp = word[i]
            word[i] = word[j]
            word[j] = tmp
            i += 1
            j -= 1
        return ''.join(word)