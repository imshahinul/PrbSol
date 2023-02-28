# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        out = []
        count = Counter()

        def postorder(root: Optional[TreeNode]) -> str:
            if not root:
                return ''

            encoded = str(root.val) + '#' + postorder(root.left) + '#' + postorder(root.right)
            count[encoded] += 1
            if count[encoded] == 2:
                out.append(root)
            return encoded

        postorder(root)
        return out