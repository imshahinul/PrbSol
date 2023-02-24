class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        m = math.inf
        min_heap = []
        for num in nums:
            if num % 2 == 1:
                num *= 2
            m = min(m, num)
            heappush(min_heap,-num)
        out = -min_heap[0] - m
        while min_heap[0] % 2 == 0:
            d = heappop(min_heap) // 2
            heappush(min_heap, d)
            m = min(m, -d)
            out = min(out, -min_heap[0] - m)
        return out