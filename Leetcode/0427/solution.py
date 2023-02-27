"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def sub(p, q, r, s):
            bz = bo = 0
            for i in range(p, r + 1):
                for j in range(q, s + 1):
                    if grid[i][j] == 0:
                        bz = 1
                    else:
                        bo = 1
            isLeaf = bz + bo == 1
            val = isLeaf and bo
            if isLeaf:
                return Node(grid[p][q], True)
            topLeft = sub(p, q, (p + r) // 2, (q + s) // 2)
            topRight = sub(p, (q + s) // 2 + 1, (p + r) // 2, s)
            bottomLeft = sub((p + r) // 2 + 1, q, r, (q + s) // 2)
            bottomRight = sub((p + r) // 2 + 1, (q + s) // 2 + 1, r, s)
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        return sub(0, 0, len(grid) - 1, len(grid[0]) - 1)