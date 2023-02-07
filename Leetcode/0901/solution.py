class StockSpanner:

    def __init__(self):
        self.ms = [[math.inf, 0]]

    def next(self, price: int) -> int:
        d = self.ms[-1][1] + 1
        while price >= self.ms[-1][0]:
            self.ms.pop(-1)
        stkspn = d - self.ms[-1][1]
        self.ms.append([price, d])
        return stkspn


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)