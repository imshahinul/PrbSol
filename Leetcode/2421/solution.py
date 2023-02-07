class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self,x,y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1



class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        values_to_nodes = {}
        for i, v in enumerate(vals):
            values_to_nodes.setdefault(v, []).append(i)

        dsu = UnionFind(n)
        good_paths = 0
        for vs, ns in sorted(values_to_nodes.items()):
            for n in ns:
                for neig in adj[n]:
                    if vals[n] >= vals[neig]:
                        dsu.union_set(n, neig)

            group = {}
            for n in ns:
                group[dsu.find(n)] = group.get(dsu.find(n), 0) + 1

            for size in group.values():
                good_paths += (size * (size + 1)) // 2

        return good_paths