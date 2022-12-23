class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l = len(nums)
        left_sum = 0
        for i in range(l):
            right_sum = t - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1