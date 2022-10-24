class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        p_sum = 0
        time = 0
        out = 0
        for s in satisfaction:
            if s >= 0:
                p_sum += s
                time += 1
                out += time * s

        n_sum = 0
        deductable = 0
        n_time = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] < 0:
                total = n_sum + satisfaction[i]
                if p_sum + total > 0:
                    deductable += total
                    n_sum += satisfaction[i]
                    n_time += 1
                else:
                    break

        return out + (p_sum * n_time) + deductable

