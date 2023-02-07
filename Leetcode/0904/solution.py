class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        out = 0
        ctr = defaultdict(int)

        l = 0
        for i, node in enumerate(tree):
            ctr[node] += 1
            while len(ctr) > 2:
                ctr[tree[l]] -= 1
                if ctr[tree[l]] == 0:
                    del ctr[tree[l]]
                l += 1
            out = max(out, i - l + 1)

        return out