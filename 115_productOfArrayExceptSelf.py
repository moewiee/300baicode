class Solution:
    def productExceptSelf(self, nums: list) -> list:
        product = [1 for _ in range(len(nums)+1)]
        product_reverse = [1 for _ in range(len(nums)+1)]
        runningProduct = 1
        for i, n in enumerate(nums):
            runningProduct *= n
            product[i+1] = runningProduct
        
        runningProduct = 1
        for i, n in enumerate(nums[::-1]):
            runningProduct *= n
            product_reverse[i+1] = runningProduct
        
        return [product[i]*product_reverse[len(nums) - i - 1] for i in range(len(nums))]
            