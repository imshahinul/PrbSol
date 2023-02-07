class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        mod = set(nums1)

        for num in nums2:
          if num in mod:
            out.append(num)
            mod.remove(num)

        return out