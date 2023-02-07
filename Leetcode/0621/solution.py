class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ctr = Counter(tasks)
        max_val = max(ctr.values())
        max_val_need = (max_val - 1) * (n + 1)
        no_max_val = sum(value == max_val for value in ctr.values())
        return max(max_val_need + no_max_val, len(tasks))