class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oc = 0
        fc = 0
        for ch in s:
            if ch == '1':
                oc += 1
            else:
                if oc >= 1:
                    fc += 1
            fc = min(fc, oc)
        return fc