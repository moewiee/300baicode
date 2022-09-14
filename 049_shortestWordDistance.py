class Solution:
    def shortestDistance(self, wordsDict: list, word1: str, word2: str) -> int:
        w1 = None
        w2 = None
        min_dist = 10000
        for i, word in enumerate(wordsDict):
            if word == word1: 
                w1 = i
                if w2 is not None:
                    dist = abs(i) - w2
                    min_dist = min(dist, min_dist)
            elif word == word2: 
                w2 = i
                if w1 is not None:
                    dist = abs(i) - w1
                    min_dist = min(dist, min_dist)
                        
        return min_dist
            