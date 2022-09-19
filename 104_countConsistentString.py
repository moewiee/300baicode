class Solution:
    def countConsistentStrings(self, allowed: str, words: list) -> int:
        allowed = set(allowed)
        ret = 0
        for w in words:
            flag = 1
            for ch in w:
                if ch not in allowed:
                    flag = 0
                    break
            if flag: ret += 1
        return ret