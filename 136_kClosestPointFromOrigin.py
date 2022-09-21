import heapq
List = list

class Solution:
    def distanceFromOrigin(self, point):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = []
        distanceMap = {}
        heapq.heapify(stack)
        for point in points:
            distance = self.distanceFromOrigin(point)
            if distance in distanceMap:
                distanceMap[distance] += [point]
            else:
                distanceMap[distance] = [point]
            heapq.heappush(stack, - distance)
            if len(stack) > k:
                heapq.heappop(stack)
        
        stack = set(stack)
        return [f for dist in stack for f in distanceMap[-dist]]
        