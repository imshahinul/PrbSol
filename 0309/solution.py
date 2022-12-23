class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown = 0
        sell = 0
        hold = -math.inf
        for price in prices:
            prev_cooldown = cooldown
            prev_sell = sell
            prev_hold = hold
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cooldown - price)
        return max(sell, cooldown)
