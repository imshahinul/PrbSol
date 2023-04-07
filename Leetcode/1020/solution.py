class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        out = 0
        m, n = len(grid), len(grid[0])

        def is_enclosed(i, j):
            nonlocal c
            if grid[i][j] == 0:
                return True
            if i <= 0 or i >= m - 1 or j <= 0 or j >= n - 1:
                return False
            grid[i][j] = 0
            c += 1
            b = True
            for x, y in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                b = is_enclosed(x, y) and b
            return b

        for i in range(m):
            for j in range(n):
                c = 0
                if is_enclosed(i, j):
                    out += c
        return out