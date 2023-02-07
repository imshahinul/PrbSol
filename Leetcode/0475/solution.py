class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        end = len(heaters) - 1
        out = 0
        p = 0
        q = 0
        for h in houses:
            while q < end and h > heaters[q]:
                p, q = q, q + 1
            r_l = abs(heaters[p] - h)
            r_r = abs(heaters[q] - h)
            out = max(out, min(r_l,r_r))
        return out