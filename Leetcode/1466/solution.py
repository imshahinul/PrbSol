class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x,y in connections:
            adj[x].append((y,1))
            adj[y].append((x,0))
        dq = deque()
        dq.append(0)
        out = 0
        traversed = [False] * n
        traversed[0] = True
        while len(dq) > 0:
            curr = dq.popleft()
            for y, c in adj[curr]:
                if not traversed[y]:
                    traversed[y] = True
                    out += c
                    dq.append(y)
        return out