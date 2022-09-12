binary_search = __import__('019_binarySearch')

class Solution:
    def __init__(self):
        self.binary_searcher = binary_search.Solution()
    
    def twoSum(self, numbers: list, target: int) -> list:
        for i, n in enumerate(numbers):
            remainer = target - n
            remainer_index = self.binary_searcher.search(numbers, remainer)
            if remainer_index != -1:
                if remainer_index == i:
                    return [i + 1, remainer_index + 2]
                else:
                    return [i + 1, remainer_index + 1]
        

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))        