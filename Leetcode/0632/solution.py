class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums1 = [(num[0],i,0) for i,num in enumerate(nums)]
        heapq.heapify(nums1)
        elm_a = -10**5 - 1
        elm_b = 10**5 + 1
        b = max(num[0] for num in nums)
        while nums1:
            a, i, j = heapq.heappop(nums1)
            if b - a < elm_b - elm_a:
                elm_a, elm_b = a, b
            if j+1 == len(nums[i]):
                return elm_a, elm_b
            b = max(b,nums[i][j+1])
            heapq.heappush(nums1,(nums[i][j+1],i,j+1))