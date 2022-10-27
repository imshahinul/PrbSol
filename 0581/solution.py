class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l = -1
        u = -1
        max_num = nums[0]
        min_num = nums[n]

        for i in range(1, len(nums)):
            x = nums[i]
            y = nums[n - i]

            if x < max_num:
                u = i
            else:
                max_num = x
            if y > min_num:
                l = i
            else:
                min_num = y

        return max(0, l + u - n + 1)