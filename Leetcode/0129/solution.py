# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        out = 0

        def rec_dfs(root: Optional[TreeNode], path: int) -> None:
            nonlocal out
            if not root:
                return
            if not root.left and not root.right:
                out += path * 10 + root.val
                return

            rec_dfs(root.left, path * 10 + root.val)
            rec_dfs(root.right, path * 10 + root.val)

        rec_dfs(root, 0)
        return out