"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []
        if root is None:
            return out
        stk = [root]
        while stk:
            root = stk.pop()
            for ch in root.children:
                stk.append(ch)
            out.append(root.val)
        return out[::-1]