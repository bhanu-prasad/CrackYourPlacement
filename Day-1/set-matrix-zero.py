class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        for i in zeros:
            n = i[0]
            temp = 0
            while temp < len(matrix[0]):
                matrix[n][temp] = 0
                temp+=1
            m = i[1]
            temp = 0
            while temp < len(matrix):
                matrix[temp][m] = 0
                temp+=1
        return matrix