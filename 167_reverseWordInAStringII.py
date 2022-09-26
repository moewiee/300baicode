class Solution:
    def reverseWords(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
            
        i = 0
        j = 0
        while j < len(s):
            if s[j] == " ":
                k = j - 1
                while i < k:
                    tmp = s[i]
                    s[i] = s[k]
                    s[k] = tmp
                    i += 1
                    k -= 1
                j += 1
                i = j
            else:
                j += 1
        
        
        k = j - 1
        while i < k:
            tmp = s[i]
            s[i] = s[k]
            s[k] = tmp
            i += 1
            k -= 1
