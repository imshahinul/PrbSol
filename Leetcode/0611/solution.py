class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        out = 0
        for hypo in range(len(nums) - 1, 1, -1):
            i = 0
            j = hypo - 1
            while i < j:
                if nums[i] + nums[j] > nums[hypo]:
                    out += j - i
                    j -= 1
                else:
                    i += 1

        return out