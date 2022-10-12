class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        out = []
        for elm in arr:
            if len(out) == 0 or out[-1] <= elm:
                out.append(elm)
            else:
                max_elm = out[-1]
                while out and out[-1] > elm:
                    max_elm = max(max_elm, out.pop())
                out.append(max_elm)

        return len(out)