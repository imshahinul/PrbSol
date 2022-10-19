class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        sum_w = 0
        n = len(nums)
        f_s = [nums[0]] * n
        l_s = [nums[-1]] * n

        for i in range(1, n):
            f_s[i] = f_s[i - 1] + nums[i]
            l_s[i] = l_s[i - 1] + nums[n - 1 - i]

        for i in range(n - 1):
            sum_w += (1 << i) * (l_s[i] - f_s[i])
            sum_w %= 10 ** 9 + 7

        return sum_w