# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def rec_build(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if not inorder or not postorder:
                return
            root = TreeNode(postorder.pop())
            mp = inorder.index(root.val)
            root.right = rec_build(inorder[mp + 1:], postorder)
            root.left = rec_build(inorder[:mp], postorder)
            return root

        return rec_build(inorder, postorder)