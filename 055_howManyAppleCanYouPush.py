import heapq

class Solution:
    def maxNumberOfApples(self, weight: list) -> int:
        heapq.heapify(weight)
        bucket_weights = 0
        apple_count = 0
        
        while weight and bucket_weights <= 5000:
            next_apple = heapq.heappop(weight)
            if bucket_weights + next_apple <= 5000:
                apple_count += 1
                bucket_weights += next_apple
            else:
                return apple_count
        
        return apple_count
                