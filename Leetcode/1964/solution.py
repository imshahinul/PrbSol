class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        bucket = []
        ans = []

        for i in range(n):
            idx = bisect.bisect_right(bucket, obstacles[i])
            if idx == len(bucket):
                bucket.append(obstacles[i])
            else:
                bucket[idx] = obstacles[i]
            ans.append(idx + 1)

        return ans