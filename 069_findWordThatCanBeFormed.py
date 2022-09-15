class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        d_char = {}
        ret = 0
        for ch in chars:
            d_char[ch] = d_char[ch] + 1 if ch in d_char.keys() else 1
        for word in words:
            d_word = {}
            flag = 1
            for ch in word:
                d_word[ch] = d_word[ch] + 1 if ch in d_word.keys() else 1
            for ch in d_word.keys():
                if ch not in d_char.keys() or d_word[ch] > d_char[ch]:
                    flag = 0
                    break
            if flag:
                ret += len(word)

        return ret