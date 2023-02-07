# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.out = 0
        def dfs(root,mini=math.inf,maxi=-math.inf):
            if root:
                mini = min(mini,root.val)
                maxi = max(maxi, root.val)
                dfs(root.left, mini,maxi)
                dfs(root.right, mini, maxi)
            else:
                self.out = max(self.out, maxi - mini)
        dfs(root)
        return self.out