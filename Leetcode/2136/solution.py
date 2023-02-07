class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        interval = 0
        out = 0
        for pt, gt in sorted([(pt, gt) for (pt, gt) in zip(plantTime, growTime)], key=lambda x: -x[1]):
            interval += pt
            out = max(out, interval + gt)

        return out