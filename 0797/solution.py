class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        out = []

        def dfs(x, p):
            if x == len(graph) - 1:
                out.append(p)
                return
            for y in graph[x]:
                dfs(y, p + [y])

        dfs(0, [0])
        return out