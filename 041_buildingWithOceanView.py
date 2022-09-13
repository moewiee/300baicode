class Solution:
    def findBuildings(self, heights: list) -> list:
        stack = []
        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
            else:
                if h >= stack[-1][1]:
                    while len(stack) > 0 and h >= stack[-1][1]:
                        stack.pop()
                    stack.append([i, h])
                else:
                    stack.append([i, h])
                        
        return [f[0] for f in stack]