class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        out = -1
        flag = False
        while dq:
            out += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    a, b = i + x, y + j
                    if 0 <= a < n and 0 <= b < n and grid[a][b] == 0:
                        flag = True
                        grid[a][b] = 1
                        dq.append((a, b))
        return out if flag else -1