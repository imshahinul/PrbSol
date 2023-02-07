class Solution:
    def mySqrt(self, x: int) -> int:
        l, u = 0, x+1
        while l < u:
            m = (l + u) // 2
            if m * m <= x:
                l = m + 1
            else:
                u = m
        return l - 1