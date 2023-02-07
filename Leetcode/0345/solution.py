class Solution:
    def reverseVowels(self, s: str) -> str:
        c_list = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and c_list[l].lower() not in vowels:
                l += 1
            while l < r and c_list[r].lower() not in vowels:
                r -= 1
            c_list[l], c_list[r] = c_list[r], c_list[l]
            l += 1
            r -= 1

        return ''.join(c_list)