class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        seen = set()

        def dfs(u):
            if u in seen: return
            seen.add(u)
            for v in range(n):
                if u == v:
                    continue
                if v in seen:
                    continue
                x1, y1 = stones[u][0], stones[u][1]
                x2, y2 = stones[v][0], stones[v][1]
                if x1 == x2:
                    dfs(v)
                if y1 == y2:
                    dfs(v)

        no_of_islands = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                no_of_islands += 1
        return n - no_of_islands