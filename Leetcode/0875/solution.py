class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, int(1e9)
        while low < high:
            mid = (low + high) >> 1
            s = sum((p + mid - 1) // mid for p in piles)
            if s <= h:
                high = mid
            else:
                low = mid + 1
        return low