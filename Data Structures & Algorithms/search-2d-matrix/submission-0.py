class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        
        while low <= high:
            middle_index = (low + high) // 2

            if matrix[middle_index][0] <= target <= matrix[middle_index][-1]:
                for j in matrix[middle_index]:
                    if j == target:
                        return True
                return False
            if target < matrix[middle_index][0]:
                high = middle_index - 1
            if target > matrix[middle_index][-1]:
                low = middle_index + 1

        return False
                
        


                
