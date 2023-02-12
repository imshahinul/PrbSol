class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for x, y in roads:
            adj[x].append(y)
            adj[y].append(x)

        def sub(child, parent):
            tp = 1
            tf = 0
            for y in adj[child]:
                if y != parent:
                    p, f = sub(y, child)
                    tp += p
                    tf += f + ((p + seats - 1) // seats)
            return (tp, tf)

        fp, ff = sub(0, -1)
        return ff