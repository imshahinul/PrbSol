class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                m_i = math.inf
                for p in range(max(0, j - 1), min(n, j + 2)):
                    m_i = min(m_i, matrix[i - 1][p])
                matrix[i][j] += m_i
        return min(matrix[-1])