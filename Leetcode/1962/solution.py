class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            x = heapq.heappop(piles)
            heapq.heappush(piles, x//2)
        return sum([-p for p in piles])