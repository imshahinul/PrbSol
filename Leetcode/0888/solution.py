class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_bob = sum(bobSizes)
        total_alice = sum(aliceSizes)
        unique_bob = set(bobSizes)
        for alice_box in aliceSizes:
            if alice_box + (total_bob - total_alice) /2 in unique_bob:
                return [alice_box, alice_box + (total_bob - total_alice) /2]