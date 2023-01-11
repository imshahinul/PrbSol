class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        bucket = [[] for _ in range(n)]
        for u, v in edges:
            bucket[u].append(v)
            bucket[v].append(u)
        traversed = set()

        def dfs(root):
            if root in traversed:
                return 0
            traversed.add(root)
            t = 0
            for child in bucket[root]:
                t += dfs(child)
            if t > 0:
                return t + 2
            return 2 if hasApple[root] else 0

        return max(dfs(0) - 2, 0)