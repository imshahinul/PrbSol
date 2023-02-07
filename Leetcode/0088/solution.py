class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ = nums1[0:m]
        tmp = []
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                tmp.append(nums1_.pop(0))
            else:
                tmp.append(nums2.pop(0))
        if nums1_:
            tmp += nums1_
        else:
            tmp += nums2
        nums1[:] = tmp[:]