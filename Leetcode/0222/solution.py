# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dep(tree):
            if tree == None:
                return 0
            return 1 + dep(tree.left)
        
        if root == None:
            return 0
        left_hand = dep(root.left)
        right_hand = dep(root.right)
        if left_hand == right_hand:
            return (1 << left_hand) + self.countNodes(root.right)
        else:
            return (1 << (left_hand - 1)) + self.countNodes(root.left)