class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        out = []
        for i in range(len(nums)):
            if dq and i - k > dq[0] - 1:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out