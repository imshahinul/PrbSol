class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr = Counter(s1)
        need = len(s1)
        for i, c in enumerate(s2):
            cntr[c] -= 1
            if cntr[c] >= 0:
                need -= 1
            if i >= len(s1):
                cntr[s2[i - len(s1)]] += 1
                if cntr[s2[i - len(s1)]] > 0:
                    need += 1
            if need == 0:
                return True
        return False