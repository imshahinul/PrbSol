class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        def sub(s):
            lb, ub = 0, n
            while lb < ub:
                mid = (lb + ub) // 2
                if s * potions[mid] >= success:
                    ub = mid
                else:
                    lb = mid + 1
            return lb
        return [n - sub(s) for s in spells]