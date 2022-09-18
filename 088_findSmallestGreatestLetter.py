searchInsert = __import__('079_searchInsert')

class Solution:
    def __init__(self):
        self.algo = searchInsert.Solution()
    
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        insert_idx = self.algo.searchInsert(letters, target)
        while insert_idx < len(letters) and letters[insert_idx] == target:
            insert_idx += 1
        
        return letters[insert_idx]
        