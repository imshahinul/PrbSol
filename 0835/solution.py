class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img11 = []
        img21 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img11.append([i, j])
                if img2[i][j] == 1:
                    img21.append([i, j])

        dd = defaultdict(int)
        for i1 in img11:
            for i2 in img21:
                dd[(i1[0] - i2[0]) * 100 + (i1[1] - i2[1])] += 1

        return max(dd.values() if dd else [0])