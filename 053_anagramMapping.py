class Solution:
    def anagramMappings(self, nums1: list, nums2: list) -> list:
        d = {}
        for i, n in enumerate(nums2):
            d[n] = [i] if n not in d.keys() else d[n] + [i]

        ret = []
        for n in nums1:
            ret.append(d[n].pop())

        return ret