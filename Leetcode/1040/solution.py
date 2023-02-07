class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        return [self.min_move(stones), self.max_move(stones)]

    def min_move(self, stones):
        min_mv = math.inf
        l = 0
        for r in range(1, len(stones)):
            while stones[r] - stones[l] >= len(
                    stones):
                l += 1
            if stones[r] - stones[l] == len(stones) - 2 and r - l + 1 == len(
                    stones) - 1:
                min_mv = min(min_mv, 2)
            else:
                min_mv = min(min_mv, len(stones) - (r - l + 1))
        return min_mv

    def max_move(self, stones):
        return max(1 + (stones[-1] - len(stones) + 1) - stones[1], 1 + stones[-2] - (stones[0] + len(stones) - 1))
