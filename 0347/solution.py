class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out=[]
        d = collections.Counter(nums)
        for idx, rw in d.items():
            if len(out)<k:
                heapq.heappush(out,(rw,idx))
            else:
                heapq.heappush(out,(rw,idx))
                heapq.heappop(out)
        return [idx for rw, idx in out]