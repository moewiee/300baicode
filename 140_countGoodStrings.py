class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        currentChars = {}
        for ch in s[:3]:
            if ch in currentChars:
                currentChars[ch] += 1
            else:
                currentChars[ch] = 1
        if len(currentChars) == 3:
            count = 1
        else:
            count = 0
            
        l = 0
        r = 2
        
        while r < len(s) - 1:
            r += 1
            if s[r] in currentChars:
                currentChars[s[r]] += 1
            else:
                currentChars[s[r]] = 1
            currentChars[s[l]] -= 1
            if currentChars[s[l]] == 0:
                del currentChars[s[l]]
            if len(currentChars) == 3:
                count += 1
            l += 1
            
        return count
