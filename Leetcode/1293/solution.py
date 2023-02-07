class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ml = len(grid)
        nl = len(grid[0])
        goal = (ml - 1, nl - 1)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        dq = deque([(0, (0, 0, k))])

        visited = set([(0, 0, k)])

        while dq:
            no_of_steps, (m, n, remaining) = dq.popleft()
            if (m, n) == goal:
                return no_of_steps

            for x, y in directions:
                next_m = m + x
                next_n = n + y

                if (ml > next_m >= 0) and (nl > next_n >= 0):
                    next_remaining = remaining - grid[next_m][next_n]

                    if next_remaining >= 0 and (next_m, next_n, next_remaining) not in visited:
                        visited.add((next_m, next_n, next_remaining))
                        dq.append((no_of_steps + 1, (next_m, next_n, next_remaining)))

        return -1