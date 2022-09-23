class Solution:
    def countWords(self, words1: list, words2: list) -> int:
        d1 = set()
        d2 = set()
        more_than_once = set()
        for w in words1:
            if w not in d1: d1.add(w)
            else: more_than_once.add(w)
        for w in words2:
            if w not in d2: d2.add(w)
            else: more_than_once.add(w)
        
        return len(d1.intersection(d2) - more_than_once)