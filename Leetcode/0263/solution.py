class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if i not in [2, 3, 5]:
                    return False
        if n > 1 and n not in [2, 3, 5]:
            return False
        return True
