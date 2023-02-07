class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for s, d, w in flights:
            g[s].append((d,w))

        pq = [(0, src, k + 1)]
        dist = [[math.inf] * (k + 2) for _ in range(n)]
        while pq:
            weight, source, stops = heapq.heappop(pq)
            if source == dst:
                return weight
            if stops > 0:
                for d, w in g[source]:
                    if weight + w < dist[d][stops - 1]:
                        dist[d][stops - 1] = weight + w
                        heapq.heappush(pq, (weight + w, d, stops - 1))
        return -1