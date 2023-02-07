class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        out = 0
        buckets = [0] * 121
        for a in ages:
            buckets[a] += 1

        for x, xc in enumerate(buckets):
            for y, yc in enumerate(buckets):
                if x < y:
                    continue
                if x < 100 < y:
                    continue
                if 0.5 * x + 7 >= y:
                    continue
                out += xc * yc
                if x == y:
                    out -= xc
        return out