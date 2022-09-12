class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        remain = 0

        ch_dict = {}
        for ch in s:
            if ch in ch_dict.keys():
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1

        for ch in ch_dict.keys():
            if ch_dict[ch] % 2 == 0:
                longest += ch_dict[ch]
            else:
                longest += ch_dict[ch] - 1
                remain = 1
        
        if remain:
            longest += 1

        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('a'))