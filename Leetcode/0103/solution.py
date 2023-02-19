# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ltr = True
        curr = [root]
        out = []
        while curr:
            next = []
            curr_val = []
            for node in curr:
                curr_val.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if ltr:
                out.append(curr_val)
            else:
                out.append(curr_val[::-1])
            ltr = not ltr
            curr = next
        return out