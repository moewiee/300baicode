class Solution:
    def shortestWordDistance(self, wordsDict: list, word1: str, word2: str) -> int:
        d = {}
        for i, w in enumerate(wordsDict):
            if w not in d: d[w] = [i]
            else: d[w].append(i)
        
        shortestDistance = 200000
        if word1 != word2:
            idxOne = d[word1]
            idxTwo = d[word2]
            i = 0
            j = 0
            while i < len(idxOne) and j < len(idxTwo):
                shortestDistance = min(shortestDistance, abs(idxOne[i] - idxTwo[j]))
                if idxOne[i] <= idxTwo[j]: i += 1
                else: j += 1
            while i < len(idxOne):
                shortestDistance = min(shortestDistance, abs(idxOne[i] - idxTwo[-1]))
                i += 1
            while j < len(idxTwo):
                shortestDistance = min(shortestDistance, abs(idxOne[-1] - idxTwo[j]))
                j += 1
        else:
            idxArray = d[word1]
            for i in range(1, len(idxArray)):
                shortestDistance = min(shortestDistance, idxArray[i] - idxArray[i-1])

        return shortestDistance