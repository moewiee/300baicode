class Solution:
    def canThreePartsEqualSum(self, arr: list) -> bool:
        totalSum = sum(arr)
        if totalSum % 3: return False
        thirdSum = int(totalSum / 3)
        
        i = 0
        currentSum = 0
        blankSum = 1
        while i < len(arr) and (currentSum != thirdSum or blankSum):
            currentSum += arr[i]
            blankSum = 0
            i += 1
        if i == len(arr): return False
        
        currentSum = 0
        blankSum = 1
        while i < len(arr) and (currentSum != thirdSum or blankSum):
            currentSum += arr[i]
            blankSum = 0
            i += 1
        if i == len(arr): return False
        
        return True