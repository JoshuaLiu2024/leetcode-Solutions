class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 剥皮算法：
        # 收集第一行，然后去除第一行，逆时针旋转矩阵，继续收集第一行，重复上面的步骤
        result = list()
        num = len(matrix) * len(matrix[0])

        def matrix_rotate(matrix):
            return [list(row) for row in zip(*matrix)][::-1]

        while len(result) != num :
            for val in matrix[0]:
                result.append(val)
            del matrix[0]
            matrix = matrix_rotate(matrix)
        return result