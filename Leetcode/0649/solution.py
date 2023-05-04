class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n,r,d = len(senate),deque(),deque()
        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            idx_r = r.popleft()
            idx_d = d.popleft()
            if idx_r < idx_d:
                r.append(idx_r + n)
            else:
                d.append(idx_d + n)
        return 'Dire' if not r else 'Radiant'