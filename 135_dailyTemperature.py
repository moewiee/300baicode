List = list

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmerAfter = [0 for _ in range(len(temperatures))]
        monoStack = []
        for i, t in enumerate(temperatures):
            while monoStack and t > temperatures[monoStack[-1]]:
                warmerAfter[monoStack[-1]] = i - monoStack[-1]
                monoStack.pop()
            monoStack.append(i)
                
        return warmerAfter