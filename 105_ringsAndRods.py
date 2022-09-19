class Solution:
    def __init__(self):
        self.rod = [set() for _ in range(10)]
    def countPoints(self, rings: str) -> int:
        for i in range(0, len(rings), 2):
            self.rod[int(rings[i+1])].add(rings[i])
        return sum([1 for r in self.rod if len(r) == 3])