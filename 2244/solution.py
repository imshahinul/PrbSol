class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic_vals = Counter(tasks).values()
        if 1 in dic_vals:
            return -1
        return sum((v + 2) // 3 for v in dic_vals)