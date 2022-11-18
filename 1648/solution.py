class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        lb,ub = 0, max(inventory)
        while ub - lb > 1:
            m = lb + (ub - lb) // 2
            t = sum(inv - m for inv in inventory if inv > m)
            if t > orders:
                lb = m
            else:
                ub = m
        t = out = 0
        for inv in inventory:
            if inv > ub:
                t += (inv - ub)
                out += (inv * (inv + 1) // 2) - (ub * (ub + 1) // 2)
        if t < orders:
            out += (orders - t) * ub
        return out % (10 ** 9 + 7)