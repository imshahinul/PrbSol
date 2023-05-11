class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        bucket = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if nums1[i] == nums2[j]:
                    bucket[i + 1][j + 1] = 1 + bucket[i][j]
                else:
                    bucket[i + 1][j + 1] = max(bucket[i][j + 1], bucket[i + 1][j])
        return bucket[l1][l2]