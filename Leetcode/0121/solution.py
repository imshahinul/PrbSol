class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out, m = 0, math.inf
        for price in prices:
            out = max(out, price - m)
            m = min(m, price)
        return out
