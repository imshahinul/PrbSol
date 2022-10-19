class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))
        cur = []
        out = 0
        for start,end in intervals:
            if not cur or start > cur[1]:
                out +=2
                cur = [end-1,end]
            elif start > cur[0]:
                out += 1
                cur = [cur[1],end]
        return out