class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i = 0
        j = 0
        longest = 0
        while j <= len(s):
            numDistict = len(set(s[i:j]))
            if numDistict <= 2:
                if j-i > longest:
                    longest = j - i
                j += 1
            else:
                i += 1
                
        return longest