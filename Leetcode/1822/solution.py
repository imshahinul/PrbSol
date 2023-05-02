class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = 1
        for num in nums:
            if num > 0:
                flag *= 1
            elif num < 0:
                flag *= -1
            else:
                return 0
        return flag