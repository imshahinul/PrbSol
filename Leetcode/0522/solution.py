class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(x, y):
            it = iter(y)
            return all(c in it for c in x)

        strs.sort(key=len, reverse=True)
        l = len(strs)
        for i in range(l):
            idx = 1
            for j in range(l):
                if (i != j and is_subseq(strs[i], strs[j])):
                    idx = 0
                    break
            if (idx): return len(strs[i])
        return -1