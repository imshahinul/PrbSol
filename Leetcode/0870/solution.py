class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = deque(sorted(nums1))
        for n2, i in sorted([-n2, i] for i, n2 in enumerate(nums2)):
            if -n2 < nums1[-1]:
                nums2[i] = nums1.pop()
            else:
                nums2[i] = nums1.popleft()
        return nums2