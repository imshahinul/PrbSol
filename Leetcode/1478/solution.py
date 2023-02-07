class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        buckets = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                house_pos = houses[(i + j) // 2]
                for l in range(i, j + 1):
                    buckets[i][j] += abs(house_pos - houses[l])

        @lru_cache(None)
        def position_mailbox(k, i):
            if k == 0 and i == n:
                return 0

            out = math.inf
            for j in range(i, n):
                bucket = buckets[i][j]
                out = min(out, bucket + position_mailbox(k - 1, j + 1))
            return out

        return position_mailbox(k, 0)