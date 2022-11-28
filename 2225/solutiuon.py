class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        bucket = [[] for _ in range(2)]
        print(bucket)
        l_ctr = Counter()
        for winner, losser in matches:
            if winner not in l_ctr:
                l_ctr[winner] = 0
            l_ctr[losser] += 1

        for k, v in l_ctr.items():
            if v < 2:
                bucket[v].append(k)

        return sorted(bucket[0]), sorted(bucket[1])