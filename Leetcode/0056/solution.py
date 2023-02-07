class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort(key= lambda x:x[0])
        out.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = out[-1][1]
            if curr>=intervals[i][0]:
                out[-1][1]=max(curr, intervals[i][1])
            else:
                out.append(intervals[i])
        return out