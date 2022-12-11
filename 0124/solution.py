# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = -math.inf

        def calc_max_prof(root: Optional[TreeNode]) -> int:
            nonlocal out
            if not root:
                return 0
            left = max(0, calc_max_prof(root.left))
            right = max(0, calc_max_prof(root.right))
            out = max(out, root.val + left + right)
            return root.val + max(left, right)

        calc_max_prof(root)
        return out