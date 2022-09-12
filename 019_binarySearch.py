class Solution:
    def search(self, nums: list, target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            pivot = int((low + high) / 2)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                low = pivot + 1
            else:
                high = pivot - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 2))