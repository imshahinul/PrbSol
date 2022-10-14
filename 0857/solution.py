class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([w/q,q] for w,q in zip(wage,quality))
        paid_sum = 0
        min_cost = math.inf
        offers = []
        for r,q in workers:
            heapq.heappush(offers,-q)
            paid_sum += q
            if len(offers) > k:
                paid_sum += heapq.heappop(offers)
            if len(offers) == k:
                min_cost = min(min_cost, paid_sum * r)
        return min_cost