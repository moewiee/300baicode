class Solution:
    def isCovered(self, ranges: list, left: int, right: int) -> bool:
        arr = [0 for _ in range(51)]
        for r in ranges:
            for i in range(r[0], r[1]+1):
                arr[i] = 1
        return all(arr[left:right+1])