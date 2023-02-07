class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            ctr = Counter(row)
            ctr['.'] = 1
            if max(ctr.values()) > 1:
                return False

        transposed_board = [list(sublist) for sublist in list(zip(*board))]
        for row in transposed_board:
            ctr = Counter(row)
            ctr['.'] = 1
            if max(ctr.values()) > 1:
                return False

        sj = 0
        for l in range(3):
            si = 0
            for k in range(3):
                seen = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        curr = board[i + si][j + sj]
                        if curr != '.' and curr not in seen:
                            seen.add(curr)
                        elif curr != '.' and curr in seen:
                            return False
                si += 3
            sj += 3

        return True