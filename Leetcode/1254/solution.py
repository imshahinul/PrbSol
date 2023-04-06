class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        q, out = [], 0
        m, n = len(grid), len(grid[0])
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    grid[i][j] = 1
                    is_closed = True
                    while q:
                        curr_i, curr_j = q.pop()
                        if curr_i in (0, m - 1) or curr_j in (0, n - 1):
                            is_closed = False
                        for d in dirs:
                            new_i =  curr_i + d[0]
                            new_j =  curr_j + d[1]

                            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                                q.append((new_i, new_j))
                                grid[new_i][new_j] = 1
                    if is_closed:
                        out += 1
        return out