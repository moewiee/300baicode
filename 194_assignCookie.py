class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        while len(s) - j > len(g): j += 1
        while i < len(g) and j < len(s):
            while j < len(s) and g[i] > s[j]: j += 1
            if i < len(g) and j <len(s) and g[i] <= s[j]: count += 1
            i += 1
            j += 1
            
        return count