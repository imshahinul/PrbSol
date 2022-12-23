class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        noa = 0
        prev_arr = -math.inf
        for p in sorted(points, key=lambda x:x[1]):
            if p[0] > prev_arr:
                prev_arr = p[1]
                noa += 1
        return noa