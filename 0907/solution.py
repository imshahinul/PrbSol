class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        sum = 0
        prev = [-1] * n
        next = [n] * n
        stack = []

        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] > a:
                index = stack.pop()
                next[index] = i
            if stack:
                prev[i] = stack[-1]
            stack.append(i)

        for i, a in enumerate(arr):
            sum += a * (i - prev[i]) * (next[i] - i)
        return sum % 1000000007