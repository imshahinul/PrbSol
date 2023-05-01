class Solution:
    def average(self, salary: List[int]) -> float:
        return float(sum(sorted(salary)[1:-1]))/float(len(salary)-2)