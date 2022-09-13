class Solution:
    def minOperations(self, logs) -> int:
        stack = []
        for op in logs:
            if op == './':
                pass
            elif op == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(1)

        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.minOperations(["d1/","d2/","../","d21/","./"]) == 2
    assert s.minOperations(["d1/","d2/","./","d3/","../","d31/"]) == 3
    assert s.minOperations(["d1/","../","../","../"]) == 0

    print("TEST PASSED!")