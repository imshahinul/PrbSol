class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start_x, start_y, dest_x, dest_y = 0, 0, 0, 0
        empty = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    start_x, start_y = x, y
                elif grid[x][y] == 2:
                    dest_x, dest_y = x, y
                elif grid[x][y] == 0:
                    empty += 1

        self.out = 0
        traversed = set()

        def dfs(x, y, traversed, move):
            if x == dest_x and y == dest_y:
                if move == empty + 1:
                    self.out += 1
                return

            if 0 <= x < m and 0 <= y < n and grid[x][y] != -1 and (x, y) not in traversed:
                traversed.add((x, y))
                for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dfs(x + i, y + j, traversed, move + 1)
                traversed.remove((x, y))

        dfs(start_x, start_y, traversed, 0)

        return self.out
