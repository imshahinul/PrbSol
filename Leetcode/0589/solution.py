"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        if root is None:
            return out
        stk = [root]
        while stk:
            root = stk.pop()
            out.append(root.val)
            for ch in root.children[::-1]:
                stk.append(ch)
        return out