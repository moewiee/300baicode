class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        num_add = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    num_add += 1
        
        num_add += len(stack)

        return num_add


if __name__ == "__main__":
    s = Solution()

    assert s.minAddToMakeValid('(((') == 3
    assert s.minAddToMakeValid('(()()))') == 1

    print("TEST PASSED!")