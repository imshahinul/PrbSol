class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1 = sorted(list(set(nums)),reverse=True)
        if len(nums1) < 3:
            return nums1[0]
        else:
            return nums1[2]