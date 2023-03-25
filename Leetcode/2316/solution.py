class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def sub(i, traversed):
            traversed.add(i)
            c = 1
            for j in adj[i]:
                if j not in traversed:
                    c += sub(j, traversed)
            return c

        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        traversed = set()
        out = st = 0
        for i in range(n):
            if i not in traversed:
                c1 = sub(i, traversed)
                out += st * c1
                st += c1
        return out