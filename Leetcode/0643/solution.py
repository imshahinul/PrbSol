class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = max_sum = sum(nums[:k])
        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum,window_sum)
        return max_sum / k