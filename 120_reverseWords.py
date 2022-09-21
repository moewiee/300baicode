class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ''
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return ''.join(s)
    
    def reverseWords(self, s: str) -> str:
        current = []
        ret = []
        for ch in s:
            if ch == ' ': 
                ret.append(self.reverseString(current))
                ret.append(' ')
                current = []
            else:
                current.append(ch)
        if current:
            ret.append(self.reverseString(current))

        return ''.join(ret)
                