class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_str = ''
        current_max_length = 0
        for ch in s:
            if ch not in current_str:
                current_str += ch
            else:
                idx = current_str.index(ch)
                current_str = current_str[idx+1:] + ch
            current_length = len(current_str)
            if current_length > current_max_length:
                current_max_length = current_length
                
        return current_max_length
                