class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        rowSize = len(matrix[0])
        matSize = len(matrix) * rowSize
        low = 0
        high = matSize - 1
        while low <= high:
            mid = int((high+low)/2)
            if matrix[mid//rowSize][mid%rowSize] == target:
                return True
            elif matrix[mid//rowSize][mid%rowSize] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False