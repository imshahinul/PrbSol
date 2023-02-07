class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        sm_rg = nums[-1] - nums[0]
        for n1,n2 in zip(nums,nums[1:]):
            sm_rg = min(sm_rg, max(nums[-1]-k, n1+k) - min(nums[0]+k, n2-k))
        return sm_rg