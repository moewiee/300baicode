class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        visited = {0:-1}
        running_sum = 0
        
        for i, n in enumerate(nums):
            running_sum = (running_sum + n) % k
            if running_sum in visited:
                if i - visited[running_sum] >= 2:
                    return True
            else:
                visited[running_sum] = i
        
        return False