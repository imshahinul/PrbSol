class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        flag = -1

        for i in range(len(nums)):
            if nums[i] == largest:
                flag = i
            if nums[i] != largest and largest < nums[i] * 2:
                return -1

        return flag