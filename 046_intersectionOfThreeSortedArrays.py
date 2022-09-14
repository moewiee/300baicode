class Solution:
    def arraysIntersection(self, arr1: list, arr2: list, arr3: list) -> list:
        i1 = 0
        i2 = 0
        i3 = 0
        ret = []
        
        while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3):
            if arr1[i1] == arr2[i2] and arr2[i2] == arr3[i3]:
                ret.append(arr1[i1])
                i1 += 1
                i2 += 1
                i3 += 1
            else:
                while arr1[i1] < arr2[i2] or arr1[i1] < arr3[i3]:
                    i1 += 1
                    if i1 == len(arr1): return ret
                while arr2[i2] < arr1[i1] or arr2[i2] < arr3[i3]:
                    i2 += 1
                    if i2 == len(arr2): return ret
                while arr3[i3] < arr2[i2] or arr3[i3] < arr1[i1]:
                    i3 += 1
                    if i3 == len(arr3): return ret
        
        return ret