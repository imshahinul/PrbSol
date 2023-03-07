class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = min(time) * totalTrips

        while low < high:
            mid = (low + high) >> 1
            if sum(mid // t for t in time) >= totalTrips:
                high = mid
            else:
                low = mid + 1

        return low