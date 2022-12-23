class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        p = 1
        while p < len(nums):
            k = p
            while k > 0 and int(nums[k-1]+nums[k]) < int(nums[k]+nums[k-1]):
                nums[k], nums[k-1] = nums[k-1], nums[k]
                k -= 1
            p += 1
        return str(int("".join(nums)))