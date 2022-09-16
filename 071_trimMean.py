class Solution:
    def trimMean(self, arr: list) -> float:
        k = int(len(arr) * 0.05)
        return sum(sorted(arr)[k:-k]) /(k * 18)