def solution(leftCorns: dict, rightCorns: dict, minLocation: int, maxLocation:int, startLocation:int, winSize:int):    
    leftCornPrefixSum = {} if 0 in leftCorns else {0:0}
    rightCornPrefixSum = {0: 0}
    currentSumLeft = 0
    currentSumRight = 0
    maxStepLeft = 0
    maxStepRight = 0
    for i in range(startLocation, minLocation - 1, -1):
        if i in leftCorns:
            currentSumLeft += leftCorns[i]
            leftCornPrefixSum[startLocation - i] = currentSumLeft
            maxStepLeft = max(maxStepLeft, startLocation - i)
    for i in range(startLocation + 1, maxLocation + 1, 1):
        if i in rightCorns:
            currentSumRight += rightCorns[i]
            rightCornPrefixSum[i - startLocation] = currentSumRight
            maxStepRight = max(maxStepRight, i - startLocation)

    maxAmount = 0
    
    # first go left
    for leftStep in leftCornPrefixSum:
        if leftStep >= winSize / 2:
            maxAmount = max(maxAmount, leftCornPrefixSum[leftStep])
        else:
            while maxStepRight not in rightCornPrefixSum or maxStepRight > winSize - leftStep * 2:
                maxStepRight -= 1
            maxAmount = max(maxAmount, leftCornPrefixSum[leftStep] + rightCornPrefixSum[maxStepRight])
    
    # first go right
    for rightStep in rightCornPrefixSum:
        if rightStep >= winSize / 2:
            maxAmount = max(maxAmount, rightCornPrefixSum[rightStep])
        else:
            while maxStepLeft not in leftCornPrefixSum or maxStepLeft > winSize - rightStep * 2:
                maxStepLeft -= 1
            maxAmount = max(maxAmount, leftCornPrefixSum[maxStepLeft] + rightCornPrefixSum[rightStep])
    
    return maxAmount


if __name__ == "__main__":
    input = open('173_aCorn.txt').read().splitlines()
    nCase = int(input[0])
    current_line = 1
    caseId = 1
    while nCase > 0:
        nCorn, startLocation, winSize = input[current_line].split()
        nCorn = int(nCorn)
        startLocation = int(startLocation)
        winSize = int(winSize)
        current_line += 1
        
        leftCorns = dict()
        rightCorns = dict()
        maxLocation = 0
        minLocation = 10**9
        for cornInput in range(nCorn):
            cornLocation = int(input[current_line].split()[0])
            cornAmount = int(input[current_line].split()[1])
            if abs(cornLocation - startLocation) <= winSize:
                if cornLocation <= startLocation:
                    leftCorns[cornLocation] = cornAmount
                    minLocation = min(minLocation, cornLocation)
                else:
                    rightCorns[cornLocation] = cornAmount
                    maxLocation = max(maxLocation, cornLocation)
            current_line += 1
        
        print(f'#{caseId}:', solution(leftCorns, rightCorns, minLocation, maxLocation, startLocation, winSize))
        
        caseId += 1        
        nCase -= 1