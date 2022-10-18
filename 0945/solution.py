class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ctr = {}

        def lookup(num):
            if num in ctr:
                ctr[num] = lookup(ctr[num] + 1)
            else:
                ctr[num] = num
            return ctr[num]

        return sum(lookup(num) - num for num in nums)