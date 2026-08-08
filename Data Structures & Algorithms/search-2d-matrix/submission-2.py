class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = (m * n) - 1

        while low <= high:
            middle = (low + high) // 2

            row = middle // n
            col = middle % n

            value = matrix[row][col]

            if value == target:
                return True
            elif value > target:
                high = middle - 1
            else:
                low = middle + 1
        
        return False

