class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        d = {}
        s = []
        for i in range(len(nums2)):
            while s and nums2[i] > s[-1]:
                d[s[-1]] = nums2[i]
                s.pop()
            s.append(nums2[i])
        
        while s:
            d[s[-1]] = -1
            s.pop()
        
        return [d[n] for n in nums1]