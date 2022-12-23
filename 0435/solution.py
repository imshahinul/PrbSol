class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        c = 0
        interval_end = -math.inf
        for interval in sorted(intervals,key=lambda x:x[1]):
            if interval[0] >= interval_end:
                interval_end = interval[1]
            else:
                c += 1
        return c