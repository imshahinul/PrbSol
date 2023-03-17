# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dq = deque(preorder)
        n = len(preorder)
        dc = {v: k for k, v in enumerate(inorder)}

        def rec_build(start, end):
            if start > end:
                return
            else:
                x = dq.popleft()
                root = TreeNode(x)
                mp = dc[x]
                root.left = rec_build(start, mp - 1)
                root.right = rec_build(mp + 1, end)
            return root

        return rec_build(0, n - 1)
