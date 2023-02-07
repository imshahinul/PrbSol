class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        nums = [a,b,c]
        nums.sort()
        if (nums[2] - nums[0]) == 2:
            return [0,0]
        if min(nums[1] - nums[0], nums[2] - nums[1]) <= 2:
            a = 1
        else:
            a = 2
        b = nums[2] - nums[0] - 2

        return [a,b]