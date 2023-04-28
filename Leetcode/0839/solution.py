class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        bucket = [False] * n

        def sub(idx):
            for i in range(n):
                if not bucket[i]:
                    diff = 0
                    for x, y in zip(strs[i],strs[idx]):
                        if x != y:
                            diff += 1
                        if diff > 2:
                            break
                    else:
                        bucket[i] = True
                        sub(i)


        c = 0
        for i in range(n):
            if not bucket[i]:
                c += 1
                bucket[i] = True
                sub(i)
        return c