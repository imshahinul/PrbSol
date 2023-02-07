class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0 or k == 0:
                break
            nums[i] = -nums[i]
            k -= 1
        return sum(nums) - (k % 2) * min(nums) * 2