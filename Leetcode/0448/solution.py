class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        disappeared_nums = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                disappeared_nums.append(i + 1)

        return disappeared_nums