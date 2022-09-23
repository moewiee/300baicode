class Solution:
    def checkDistances(self, s: str, distance: list) -> bool:        
        actualDistance = [0] * 26
        for i, char in enumerate(s):
            if actualDistance[ord(char)-97]:
                actualDistance[ord(char)-97] = i - actualDistance[ord(char)-97]
            else:
                actualDistance[ord(char)-97] = i
                
        print(actualDistance)
        
        for idx in range(len(actualDistance)):
            if actualDistance[idx]:
                if actualDistance[idx] != distance[idx] + 1:
                    return False
        return True
            