class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
                depth = len(stack)
                if depth > max_depth:
                    max_depth = depth

            if ch in (')', ']', '}'):
                stack.pop()

        return max_depth


if __name__ == "__main__":
    s = Solution()
    assert s.maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert s.maxDepth("(1)+((2))+(((3)))") == 3

    print('TEST PASSED!')