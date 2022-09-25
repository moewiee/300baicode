class Solution:
    def maxDistance(self, nums1: list, nums2: list) -> int:
        maxDistance = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if i > j: j += 1
            else:
                if nums1[i] > nums2[j]: i += 1
                else:
                    maxDistance = max(maxDistance, j - i)
                    j += 1
        
        return maxDistance