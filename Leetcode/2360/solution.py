class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        out,t = -1,1
        no_of_traversal = [0] * len(edges)

        for idx, edge in enumerate(edges):
            if no_of_traversal[idx]:
                continue
            start = t
            x = idx
            while x != -1 and not no_of_traversal[x]:
                no_of_traversal[x] = t
                t += 1
                x = edges[x]
            if x != -1 and no_of_traversal[x] >= start:
                out = max(out, t - no_of_traversal[x])

        return out