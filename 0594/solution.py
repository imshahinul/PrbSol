class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = Counter(nums)
        return max(v+d.get(k+1,-v) for k,v in d.items())