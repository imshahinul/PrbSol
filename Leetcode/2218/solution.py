class Solution(object):
    def maxValueOfCoins(self, piles, k):
        bucket = [0]
        for pile in piles:
            nb = [0] * min(len(bucket) + len(pile), k + 1)
            for i in range(len(bucket)):
                curr = 0
                for j in range(min(k - i, len(pile)) + 1):
                    nb[i + j] = max(nb[i + j], bucket[i] + curr)
                    curr += pile[j] if j < len(pile) else 0
            bucket = nb
        return bucket[-1]