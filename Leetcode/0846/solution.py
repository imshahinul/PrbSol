class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize == 0:
            ctr = Counter(hand)
            for h in sorted(ctr):
                while ctr[h] > 0:
                    for i in range(h,h+groupSize):
                        ctr[i] -= 1
                        if ctr[i] < 0:
                            return False
            return True
        else:
            return False