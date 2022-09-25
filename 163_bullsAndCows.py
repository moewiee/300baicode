from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numCount = Counter(secret)
        numIndices = {}
        bulls = 0
        cows = 0
        for idx, num in enumerate(secret):
            if num in numIndices:
                numIndices[num].add(idx)
            else:
                numIndices[num] = set([idx])
        
        
        for idx, num in enumerate(guess):
            if num in numCount:
                if idx in numIndices[num]:
                    bulls += 1
                    if not numCount[num] > 0:
                        numCount[num] += 1
                        cows -= 1
                else:
                    if numCount[num] > 0:
                        cows += 1
                numCount[num] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
            