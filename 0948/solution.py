class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        dq = deque(sorted(tokens))
        out = 0
        score = 0
        while dq and (dq[0] <= power or score):
            if dq[0] <= power:
                power -= dq.popleft()
                score += 1
            else:
                power += dq.pop()
                score -= 1

            out = max(out, score)
        return out