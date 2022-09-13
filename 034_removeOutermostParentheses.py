class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        p_groups = []
        current_group = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
                current_group.append(ch)
            elif ch == ')':
                stack.pop()
                current_group.append(ch)
                if len(stack) == 0:
                    p_groups.append(''.join(current_group[1:-1]))
                    current_group = []

        return ''.join(p_groups)


if __name__ == "__main__":
    s = Solution()
    assert s.removeOuterParentheses("(()())(())") == "()()()"
    assert s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert s.removeOuterParentheses("()()") == ""

    print("TEST PASSED!")