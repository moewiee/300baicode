class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        tmp = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]: 
                tmp.append(nums1[i])  
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
                
        while i < m:
            tmp.append(nums1[i])
            i += 1
        while j < n:
            tmp.append(nums2[j])
            j += 1
        for k in range(m+n):
            nums1[k] = tmp[k]