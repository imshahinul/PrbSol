class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        out = math.inf
        xy_dict = defaultdict(set)
        for x, y in points:
            xy_dict[x].add(y)

        for i in range(len(points)):
            for j in range(i):
                xa, ya = points[i]
                xb, yb = points[j]
                if xa == xb or ya == yb:
                    continue

                if yb in xy_dict[xa] and ya in xy_dict[xb]:
                    out = min(out, abs(xa - xb) * abs(ya - yb))

        if out < math.inf:
            return out
        else:
            return 0