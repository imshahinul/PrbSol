class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
        self.cnt = n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        pa, pb = self.find(a - 1), self.find(b - 1)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.parents[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.parents[pa] = pb
            self.size[pb] += self.size[pa]
        self.cnt -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        out = 0
        for t, u, v in edges:
            if t == 3:
                if alice.union(u, v):
                    bob.union(u, v)
                else:
                    out += 1
        for t, u, v in edges:
            if t == 1:
                out += not alice.union(u, v)
            if t == 2:
                out += not bob.union(u, v)
        return out if alice.cnt == 1 and bob.cnt == 1 else -1