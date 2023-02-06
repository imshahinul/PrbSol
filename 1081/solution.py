class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ms, traversed = [], set()
        cntr = {ch: i for i, ch in enumerate(s)}
        for i, ch in enumerate(s):
            if ch in traversed:
                continue
            while ms and ms[-1] > ch and cntr[ms[-1]] > i:
                traversed.remove(ms.pop())
            ms.append(ch)
            traversed.add(ch)
        return ''.join(ms)