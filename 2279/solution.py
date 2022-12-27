class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        diffs = [capacity[i] - rocks[i] for i in range(n)]
        diffs.sort()
        for i, d in enumerate(diffs):
            if d > additionalRocks:
                return i
            additionalRocks -= d
        return n