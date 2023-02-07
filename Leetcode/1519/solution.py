class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        bucket = [[] for _ in range(n)]
        for u, v in edges:
            bucket[u].append(v)
            bucket[v].append(u)

        out = [0] * n

        def dfs(p, a, counts):
            before = counts[labels[p]]

            for adj in bucket[p]:
                if adj != a:
                    dfs(adj, p, counts)

            counts[labels[p]] += 1
            out[p] = counts[labels[p]] - before

        dfs(0, 0, Counter())
        return out