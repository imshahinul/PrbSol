class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def drop(i):
            for j in range(m):
                i_nxt = i + grid[j][i]
                if i_nxt < 0 or i_nxt >= n or grid[j][i_nxt] != grid[j][i]:
                    return -1
                i = i_nxt
            return i

        return list(map(drop, range(n)))