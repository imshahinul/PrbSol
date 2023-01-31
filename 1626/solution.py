class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        comb = list(zip(ages, scores))
        comb.sort()
        bucket = [u[1] for u in comb]
        for i in range(n):
            for j in range(i):
                if comb[i][1] >= comb[j][1]:
                    bucket[i] = max(bucket[i], bucket[j] + comb[i][1])
        return max(bucket)