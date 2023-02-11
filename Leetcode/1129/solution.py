class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = [defaultdict(list), defaultdict(list)]
        for x, y in redEdges:
            adj[0][x].append(y)
        for x, y in blueEdges:
            adj[1][x].append(y)
        out = [-1] * n
        traversed = set()
        dq = deque([(0, 0), (0, 1)])
        distance = 0
        while dq:
            for _ in range(len(dq)):
                x, cnt = dq.popleft()
                if out[x] == -1:
                    out[x] = distance
                traversed.add((x, cnt))
                cnt ^= 1
                for y in adj[cnt][x]:
                    if (y, cnt) not in traversed:
                        dq.append((y, cnt))
            distance += 1
        return out