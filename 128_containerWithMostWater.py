List = list

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxContainer = 0
        while i < j:
            if height[i] < height[j]:
                maxContainer = max(maxContainer, height[i] * (j - i))
                i += 1
            else:
                maxContainer = max(maxContainer, height[j] * (j - i))
                j -= 1
        
        return maxContainer