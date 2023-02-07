class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        diff = l * (l + 1) // 2 - sum(nums)
        missing = (l * (l + 1) // 2) - sum(set(nums))
        return [missing-diff, missing]