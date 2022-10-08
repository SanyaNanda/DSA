class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        index = [(i,j) for i in range(n) for j in range(m) if matrix[i][j]==0]
        print(index)
        if len(index)!=0:
            row, col = zip(*index)
            for i in row:
                matrix[i] = [0 for _ in range(m)]
            for j in col:
                for i in range(n):
                    matrix[i][j] = 0
            # print(matrix)
# 10/05/2022 12:20	Accepted	286 ms	14.8 MB	python3
# https://leetcode.com/submissions/detail/815567998/
