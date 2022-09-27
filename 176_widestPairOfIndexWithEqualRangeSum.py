class Solution:
    def widestPairOfIndices(self, nums1: list, nums2: list) -> int:
        prefixSumA, prefixSumB = [0], [0]
        for n in nums1: prefixSumA.append(prefixSumA[-1] + n)
        for n in nums2: prefixSumB.append(prefixSumB[-1] + n)
        
        d = {}
        widestRange = 0
        for i in range(len(prefixSumA)):
            arrayDiffAtIdx = prefixSumA[i] - prefixSumB[i]
            if arrayDiffAtIdx not in d:
                d[arrayDiffAtIdx] = i
            else:
                widestRange = max(widestRange, i - d[arrayDiffAtIdx])
            
        return widestRange