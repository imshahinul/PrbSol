class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        bucket = [0] * n
        bucket[0] = nums[0]
        bucket[1] = max(nums[0],nums[1])

        for i in range(2,n):
            bucket[i] = max(bucket[i-1],bucket[i-2] + nums[i])

        return bucket[-1]