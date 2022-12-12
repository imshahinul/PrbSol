class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n, dp):
            if (n <= 1):
                return 1
            if (dp[n] != -1):
                return dp[n]
            dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
            return dp[n]

        if n == 1 or n == 2:
            return n
        buckets = [-1 for i in range(n + 1)]
        fib(n, buckets)
        return buckets[n]