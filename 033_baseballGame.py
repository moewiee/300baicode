class Solution:
    def calPoints(self, ops) -> int:
        stack = []
        for op in ops:
            if op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == "__main__":
    s = Solution()

    assert s.calPoints(["5","2","C","D","+"]) == 30
    assert s.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
    assert s.calPoints(["1","C"]) == 0

    print("TEST PASSED!")