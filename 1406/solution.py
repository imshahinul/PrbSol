class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        bucket = [0] * (n + 3)
        for i in range(n - 1, -1, -1):
            bucket[i] = max(sum(stoneValue[i:i+k]) - bucket[i+k] for k in range(1, 4))
        return 'Alice' if bucket[0] > 0 else 'Bob' if bucket[0] < 0 else 'Tie'