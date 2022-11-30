class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        return len(ctr.values()) == len(set(ctr.values()))