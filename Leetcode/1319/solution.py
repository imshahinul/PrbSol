class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        l = len(connections)
        if l < n - 1:
            return -1

        adj = defaultdict(list)
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)

        traversed = [False] * n

        def sub(i):
            dq = deque()
            dq.append(i)
            while len(dq) > 0:
                curr = dq.popleft()
                for y in adj[curr]:
                    if not traversed[y]:
                        traversed[y] = True
                        dq.append(y)

        c = 0
        for i in range(n):
            if not traversed[i]:
                c += 1
                sub(i)

        return c - 1
