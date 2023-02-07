class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        out = []
        def sub(s, path):
            if len(path) > 1:
                out.append(path)
            visited = set()
            for i in range(s, len(nums)):
                if nums[i] in visited:
                    continue
                if not path or nums[i] >= path[-1]:
                    visited.add(nums[i])
                    sub(i + 1, path + [nums[i]])
        sub(0, [])
        return out