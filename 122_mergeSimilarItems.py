class Solution:
    def mergeSimilarItems(self, items1: list, items2: list) -> list:
        d = [0 for _ in range(1001)]
        for it in items1 + items2:
            d[it[0]] += it[1]
        return [[i, f] for i, f in enumerate(d) if f]