class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]
        return grid[m-1][n-1]