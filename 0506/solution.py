class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        out = []
        score1 = sorted(score,reverse=True)
        for s in score:
            ni = score1.index(s)
            if ni == 0:
                out.append('Gold Medal')
            elif ni == 1:
                out.append('Silver Medal')
            elif ni == 2:
                out.append('Bronze Medal')
            else:
                out.append(str(ni+1))
        return out