class Solution:
    def intersect(self, p: List[int], q: List[int], r: List[int]):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        ch = []  # stack
        trees.sort(key=lambda x: (x[0], x[1]))
        for tree in trees:
            while len(ch) > 1 and self.intersect(ch[-1], ch[-2], tree) > 0:
                ch.pop()
            ch.append(tuple(tree))

        for tree in reversed(trees):
            while len(ch) > 1 and self.intersect(ch[-1], ch[-2], tree) > 0:
                ch.pop()
            ch.append(tuple(tree))

        return list(set(ch))