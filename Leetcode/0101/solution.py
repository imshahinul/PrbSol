# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_two_symmetric(self, lht: Optional[TreeNode], rht: Optional[TreeNode]) -> bool:
        if not lht or not rht:
            return lht == rht
        return lht.val == rht.val and self.check_two_symmetric(lht.left, rht.right) and self.check_two_symmetric(rht.left, lht.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_two_symmetric(root, root)