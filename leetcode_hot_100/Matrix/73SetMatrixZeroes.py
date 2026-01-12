class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 用两个布尔列表记录这行、这列是否需要置零
        m, n = len(matrix), len(matrix[0])
        flag1, flag2 = [False] * m , [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flag1[i], flag2[j] = True, True
        
        for i, val in enumerate(flag1):
            if val == True:
                matrix[i] = [0] * n
        
        for j, val in enumerate(flag2):
            if val == True:
                for i in range(m):
                    matrix[i][j]=0
        