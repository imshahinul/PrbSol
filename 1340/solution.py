class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        jumps = []

        for i in range(n + 1):
            while jumps and (i == n or arr[jumps[-1]] < arr[i]):
                indices = [jumps.pop()]
                while jumps and arr[jumps[-1]] == arr[indices[0]]:
                    indices.append(jumps.pop())
                for j in indices:
                    if i < n and i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)

                    if jumps and j - jumps[-1] <= d:
                        dp[jumps[-1]] = max(dp[jumps[-1]], dp[j] + 1)
            jumps.append(i)

        return max(dp)