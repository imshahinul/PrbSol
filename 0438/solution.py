class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntr = Counter(p)
        out = []
        lb = ub = 0
        bucket = Counter()
        while ub < len(s):
            bucket[s[ub]] += 1
            while bucket[s[ub]] > cntr[s[ub]]:
                bucket[s[lb]] -= 1
                lb += 1
            if ub - lb + 1 == len(p):
                out.append(lb)
            ub += 1
        return out