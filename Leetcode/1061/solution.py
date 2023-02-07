class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(set)
        for a, b in zip(s1, s2):
            adj[a].add(b)
            adj[b].add(a)

        dp = {}

        def sub(c):
            out = c
            visited = set()
            q = {c}

            while q:
                c = q.pop()
                if c in visited:
                    continue
                visited.add(c)
                out = min(out, c)
                q |= adj[c]

            for v in visited:
                dp[v] = out

            return out

        return ''.join(sub(c) for c in baseStr)
