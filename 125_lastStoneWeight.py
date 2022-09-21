import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-f for f in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stoneY = heapq.heappop(stones)
            stoneX = heapq.heappop(stones)
            if stoneY < stoneX:
                heapq.heappush(stones, stoneY-stoneX)
        if len(stones):
            return -stones[0]
        else:
            return 0