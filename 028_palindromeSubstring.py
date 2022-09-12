class Solution:
    def __init__(self):
        self.checked = set()
        self.palCheck = set()
        self.notPalCheck = set()
    
    def isPalindrome(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1
    
    def makePairs(self, n):
        ret = []
        for i in range(n):
            for j in range(i+1, n+1):
                ret.append([i, j])

        return ret

    def countSubstrings(self, s):
        pairs = self.makePairs(len(s))
        ret = 0
        for p in pairs:
            sub = s[p[0]:p[1]]
            if sub not in self.checked:
                if self.isPalindrome(sub):
                    self.palCheck.add(sub)
                    ret += 1
                else:
                    self.notPalCheck.add(sub)
                self.checked.add(sub)
            else:
                if sub in self.palCheck:
                    ret += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("a" * 1000))