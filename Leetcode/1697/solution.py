class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def sub(idx):
            if bucket[idx] != idx:
                bucket[idx] = sub(bucket[idx])
            return bucket[idx]

        bucket = list(range(n))
        edgeList.sort(key=lambda x: x[2])
        j = 0
        out = [False] * len(queries)
        for i, (x, y, d) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while j < len(edgeList) and edgeList[j][2] < d:
                a, b, _ = edgeList[j]
                bucket[sub(a)] = sub(b)
                j += 1
            out[i] = sub(x) == sub(y)
        return out