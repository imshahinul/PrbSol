class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        min_heap = [-gift for gift in gifts]
        heapify(min_heap)
        for _ in range(k):
            heapreplace(min_heap, -int(sqrt(-min_heap[0])))
        return -sum(min_heap)