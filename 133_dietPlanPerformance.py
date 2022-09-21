List = list

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        currentSum = sum(calories[:k])
        if currentSum < lower:
            point = -1
        elif currentSum > upper:
            point = 1
        else:
            point = 0
        
        for i in range(k, len(calories)):
            currentSum += calories[i] - calories[i-k]
            if currentSum < lower:
                point -= 1
            elif currentSum > upper:
                point += 1
        
        return point