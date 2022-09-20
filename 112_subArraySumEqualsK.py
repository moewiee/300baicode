class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        visited = {}
        count = 0
        running_sum = 0
        
        for n in nums:
            running_sum += n
            if running_sum == k:
                count += 1
            if running_sum - k in visited:
                count += visited[running_sum - k]
            if running_sum not in visited:
                visited[running_sum] = 1
            else:
                visited[running_sum] += 1
        
        return count