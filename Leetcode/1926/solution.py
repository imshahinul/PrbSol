class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        out = 0
        m,n = len(maze),len(maze[0])
        directions = [0, 1, 0, -1, 0]
        dq = deque([(entrance[0], entrance[1])])
        visited = {(entrance[0], entrance[1])}

        while dq:
            out += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                for k in range(4):
                    x = i + directions[k]
                    y = j + directions[k + 1]
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if (x, y) in visited or maze[x][y] == '+':
                        continue
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return out
                    dq.append((x, y))
                    visited.add((x, y))

        return -1