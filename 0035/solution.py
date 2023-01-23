class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1
        while l <= u:
            m = (l + u) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                u = m - 1
            else:
                l = m + 1
        return l