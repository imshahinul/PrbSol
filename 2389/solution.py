class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        def sub(query: int) -> int:
            s = 0
            for i, num in enumerate(nums):
                s += nums[i]
                if s > query:
                    return i
            return len(nums)

        return [sub(query) for query in queries]
