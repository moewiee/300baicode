class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0: return 0
        i = 0
        j = 0
        longest = 1
        d = {}
        while j < len(s):
            d[s[j]] = j
            j += 1    
            if len(d) == k + 1:
                cut_idx = min(d.values())
                d.pop(s[cut_idx])
                i = cut_idx + 1
            if j - i > longest: 
                longest = j - i                
                
        return longest


if __name__ == "__main__":
    s = Solution()
    print(
        s.lengthOfLongestSubstringKDistinct('abaccc', 2),
        s.lengthOfLongestSubstringKDistinct('eceba', 2),
        s.lengthOfLongestSubstringKDistinct('cc', 1),
    )        