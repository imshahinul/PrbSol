# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        ttl = self.dfsum(root)
        self.mp = 0
        self.dfsprd(root, ttl)
        return self.mp  % (10 ** 9 + 7)

    def dfsum(self, node):
        if node is None:
            return 0
        return self.dfsum(node.left) + self.dfsum(node.right) + node.val

    def dfsprd(self, node, ttl):
        if node is None:
            return 0
        l = self.dfsprd(node.left, ttl)
        r = self.dfsprd(node.right, ttl)
        s = l + r + node.val
        product = (ttl - s) * s
        self.mp = max(self.mp, product)
        return s