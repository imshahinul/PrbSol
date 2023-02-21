class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lb, ub = 0, len(nums) - 1

        while lb < ub:
            mid = (lb + ub) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lb = mid + 2
            else:
                ub = mid

        return nums[lb]