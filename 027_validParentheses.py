class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        q = []
        for ch in s:
            if ch in ('(', '[', '{'):
                q.append(ch)
            else:
                if not len(q):
                    return False
                if match[q.pop()] != ch:
                    return False
        if len(q):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid('([{}](()){}[]'))