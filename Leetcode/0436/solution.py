class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        l = len(intervals)
        sorted_intervals = [[intervals[i], i] for i in range(l)]
        sorted_intervals.sort()

        out = [-1] * l  # create output list with predefined -1

        def binary_search(x):
            if sorted_intervals[l - 1][0][0] < x:
                return -1;

            left, right = 0, l - 1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_intervals[mid][0][0] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            return sorted_intervals[left][1]

        for i in range(l):
            out[i] = binary_search(intervals[i][1])

        return out