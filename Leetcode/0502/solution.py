class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = list(map(list, zip(profits, capital)))
        pc.sort(key=lambda x: x[1])
        min_heap = []
        cnt = 0
        i = 0
        while cnt < k:
            while i < len(pc) and pc[i][1] <= w:
                heapq.heappush(min_heap, -pc[i][0])
                i += 1

            if min_heap:
                w += -heapq.heappop(min_heap)
                cnt += 1
            else:
                break

        return w