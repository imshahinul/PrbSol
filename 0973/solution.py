class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            neg_distance = - point[0] * point[0] - point[1] * point[1]
            heapq.heappush(max_heap, (neg_distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [mh[1] for mh in max_heap]