class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        buckets = defaultdict(list)
        out = []
        for i in range(n):
            for j in range(len(nums[i])):
                buckets[i+j].append(nums[i][j])
        for k,v in sorted(buckets.items()):
            out.extend(v[::-1])
        return out