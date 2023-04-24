class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-stone for stone in stones]
        heapq.heapify(min_heap)
        while len(min_heap) > 1:
            y, x = -heapq.heappop(min_heap), -heapq.heappop(min_heap)
            if x != y:
                heapq.heappush(min_heap, x - y)
        return 0 if not min_heap else -min_heap[0]
