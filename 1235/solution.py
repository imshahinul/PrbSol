class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_combined = sorted((st, et, p) for st, et, p in zip(startTime, endTime, profit))
        max_profit = 0
        min_heap = []
        for st, et, p in job_combined:
            while min_heap and st >= min_heap[0][0]:
                max_profit = max(max_profit, heapq.heappop(min_heap)[1])
            heapq.heappush(min_heap, (et, p + max_profit))

        return max(max_profit, max(p for e, p in min_heap))