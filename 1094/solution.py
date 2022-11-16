class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        drops = []
        for n, s, e in trips:
            drops.append((s, n))
            drops.append((e, -n))

        drops.sort()

        for _, n in drops:
            capacity -= n
            if 0 > capacity:
                return False
        return True