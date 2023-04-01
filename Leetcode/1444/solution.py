class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        p_s = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr = 1 if pizza[i][j] == 'A' else 0
                right = p_s[i][j + 1]
                bottom = p_s[i + 1][j]
                bottom_right = p_s[i + 1][j + 1]
                p_s[i][j] = curr + right + bottom - bottom_right

        memo = {}

        def rec_sub(curr_m, curr_n, k):
            if (curr_m, curr_n, k) in memo:
                return memo[(curr_m, curr_n, k)]

            if p_s[curr_m][curr_n] == 0:
                return 0

            if k == 0: return 1

            out = 0

            for i in range(curr_m + 1, m):
                if p_s[curr_m][curr_n] - p_s[i][curr_n] > 0:
                    out += rec_sub(i, curr_n, k - 1)

            for j in range(curr_n + 1, n):
                if p_s[curr_m][curr_n] - p_s[curr_m][j] > 0:
                    out += rec_sub(curr_m, j, k - 1)

            memo[(curr_m, curr_n, k)] = out

            return out

        return rec_sub(0, 0, k - 1) % 1000000007