class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack:
                if stack[-1] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()

    assert s.removeDuplicates("abbaca") == "ca"
    assert s.removeDuplicates("azxxzy") == "ay"

    print("TEST PASSED!")