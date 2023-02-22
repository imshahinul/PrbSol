class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lb = max(weights)
        ub = sum(weights)

        def check_days(ship_cap: int) -> int:
            d = 1
            cap = 0
            for weight in weights:
                if cap + weight > ship_cap:
                    d += 1
                    cap = weight
                else:
                    cap += weight
            return d

        while lb < ub:
            mid = (lb + ub) // 2
            if check_days(mid) <= days:
                ub = mid
            else:
                lb = mid + 1

        return lb