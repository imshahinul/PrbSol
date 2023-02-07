class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = round(statistics.median(nums))
        mvs = 0
        for num in nums:
            mvs += abs(med - num)

        return mvs