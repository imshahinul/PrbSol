class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ctr, pq, out = Counter(barcodes), [], []
        for n, c in ctr.items():
            heapq.heappush(pq, (-c, n))
        prev_cnt, prev_num = 0, 0
        while pq:
            cnt, num = heapq.heappop(pq)
            if prev_cnt:
                heapq.heappush(pq, (prev_cnt, prev_num))
            out.append(num)
            prev_cnt, prev_num = cnt+1, num
        return out