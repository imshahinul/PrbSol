class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        min_heap = []
        for i in range(n):
            sm = aliceValues[i] + bobValues[i]
            df = aliceValues[i] - bobValues[i]
            heapq.heappush(min_heap, (-sm, -df, aliceValues[i], bobValues[i]))
        alice = 0
        bob = 0
        is_alice = True
        while n > 0:
            sm, df, av, bv = heappop(min_heap)
            sm = -sm
            if is_alice:
                alice += av
            else:
                bob += bv
            is_alice = not is_alice
            n -= 1
        out = 0
        if alice > bob:
            out = 1
        if alice < bob:
            out = -1
        return out