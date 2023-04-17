class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx_candy = max(candies)
        return [candy + extraCandies >= mx_candy for candy in candies]