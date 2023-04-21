class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0
        dq = deque([(root, 1)])
        while dq:
            out = max(out, dq[-1][1] - dq[0][1] + 1)
            for _ in range(len(dq)):
                root, idx = dq.popleft()
                if root.left:
                    dq.append((root.left, idx << 1))
                if root.right:
                    dq.append((root.right, idx << 1 | 1))
        return out