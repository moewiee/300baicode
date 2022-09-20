class Solution:
    def subarraysDivByK(self, nums: list, k: int) -> int:
        visited = {}
        count = 0
        current = 0
        for n in nums:
            current = (current + n) % k 
            if current == 0:
                count += 1
            if current in visited:
                count += visited[current]
                visited[current] += 1
            else:
                visited[current] = 1
        
        return count