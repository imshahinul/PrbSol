class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sorted_pattern = sorted(int(m) for m in str(n))
        for i in range(30):# 2^29 is less than 10^9
            if sorted([int(m) for m in str(1 << i)]) == sorted_pattern:
                return True
        return False