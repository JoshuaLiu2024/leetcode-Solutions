class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            temp = matrix[row][col]
            if temp == target:
                return True
            elif temp < target:
                row += 1
            elif temp > target:
                col -= 1
        return False