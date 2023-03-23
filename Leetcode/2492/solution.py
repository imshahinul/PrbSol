class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y, h in roads:
            graph[x].append((y, h))
            graph[y].append((x, h))
        traversed = [False] * (n + 1)
        out = math.inf
        def sub(i):
            nonlocal out
            for j, h in graph[i]:
                out = min(out, h)
                if not traversed[j]:
                    traversed[j] = True
                    sub(j)
        sub(1)
        return out