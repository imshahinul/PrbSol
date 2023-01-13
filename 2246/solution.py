class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        out = 0
        tree = [[] for _ in range(n+1)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        def longestPathDownFrom(u: int) -> int:
            nonlocal out
            m1 = 0
            m2 = 0

            for v in tree[u]:
                result = longestPathDownFrom(v)
                if s[u] == s[v]:
                    continue
                if result > m1:
                    m2 = m1
                    m1 = result
                elif result > m2:
                    m2 = result

            out = max(out, 1+ m1 + m2)
            return 1 + m1

        longestPathDownFrom(0)
        return out