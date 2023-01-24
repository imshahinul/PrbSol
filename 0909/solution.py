class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        out = 0
        qq = collections.deque([1])
        visited = set()
        sim_board = [0] * (1 + n * n)

        for i in range(n):
            for j in range(n):
                sim_board[(n - 1 - i) * n + (j + 1 if n - i & 1 else n - j)] = board[i][j]

        while qq:
            out += 1
            for _ in range(len(qq)):
                curr = qq.popleft()
                for next in range(curr + 1, min(curr + 6, n * n) + 1):
                    tr = sim_board[next] if sim_board[next] > 0 else next
                    if tr == n * n:
                        return out
                    if tr in visited:
                        continue
                    qq.append(tr)
                    visited.add(tr)

        return -1