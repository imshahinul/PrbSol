class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.MAX = 100000
        d1 = self.sub(edges, node1)
        d2 = self.sub(edges, node2)
        out = -1
        od = self.MAX
        for i in range(len(edges)):
            if max(d1[i], d2[i]) < od:
                out = i
                od = max(d1[i], d2[i])

        return out

    def sub(self, edges, u):
        d = [self.MAX] * len(edges)
        d[u] = 0
        q= deque([u])
        while q:
            cur = q.popleft()
            nxt = edges[cur]
            if nxt != -1 and d[nxt] == self.MAX:
                d[nxt] = d[cur] + 1
                q.append(nxt)

        return d