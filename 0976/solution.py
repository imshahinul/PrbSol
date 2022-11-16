class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i,num in enumerate(nums[:-2]):
            if num < nums[i+1] + nums[i+2]:
                return num + nums[i+1] + nums[i+2]
        return 0