class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        d = {}
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in d.keys():
                    d[n] += 1
                else:
                    d[n] = 1
            k = 0
            for n in nums2:
                if n in d.keys() and d[n] > 0:
                    d[n] -= 1
                    nums1[k] = n
                    k += 1
            
            return nums1[:k]
        else:
            for n in nums2:
                if n in d.keys():
                    d[n] += 1
                else:
                    d[n] = 1
            k = 0
            for n in nums1:
                if n in d.keys() and d[n] > 0:
                    d[n] -= 1
                    nums2[k] = n
                    k += 1
            
            return nums2[:k]