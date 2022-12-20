class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        val1 = nums[0] * nums[1] * nums[2]
        val2 = nums[0] * nums[-1] * nums[-2]
        return max(val1,val2)