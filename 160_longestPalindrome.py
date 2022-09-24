class Solution:
    def expandAroundCenter(self, s, l, r):
        maxLen = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            maxLen = max(maxLen, r - l + 1)
            l -= 1
            r += 1
        
        return maxLen
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return s
        
        startOfLongestPalindrome = 0
        endOfLongestPalindrome = 0
        longestPalindrome = 0
        for i in range(len(s)):
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i+1)
            
            if l1 > l2:
                if l1 > longestPalindrome:
                    longestPalindrome = l1
                    startOfLongestPalindrome = i - int(longestPalindrome/2)
                    endOfLongestPalindrome = startOfLongestPalindrome + longestPalindrome
            else:
                if l2 > longestPalindrome:
                    longestPalindrome = l2
                    startOfLongestPalindrome = i - int(longestPalindrome / 2) + 1
                    endOfLongestPalindrome = startOfLongestPalindrome + longestPalindrome

        return s[int(startOfLongestPalindrome):int(endOfLongestPalindrome)]