class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]
        temp = {}

        def turn(i, m):
            if (i, m) in temp:
                return temp[(i, m)]
            if i + 2 * m >= n:
                res = piles[i]
                temp[(i, m)] = res
                return temp[(i, m)]
            res = piles[i] - min(turn(i + x, max(m, x)) for x in range(1, 2 * m + 1))
            temp[(i, m)] = res
            return temp[(i, m)]

        return turn(0, 1)