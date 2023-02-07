class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        t_sum = 0
        cmx_sum = 0
        cmn_sum = 0
        mx_sum = -math.inf
        min_sum = math.inf

        for num in nums:
            t_sum += num
            cmx_sum = max(cmx_sum + num, num)
            cmn_sum = min(cmn_sum + num, num)
            mx_sum = max(mx_sum, cmx_sum)
            min_sum = min(min_sum, cmn_sum)

        if mx_sum < 0:
            return mx_sum
        else:
            return max(mx_sum, t_sum - min_sum)
