class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def sub(s: str, j: int, path: List[str], out: List[List[str]]) -> None:
            if j == len(s):
                out.append(path)
                return

            for i in range(j, len(s)):
                if isPalindrome(s[j: i + 1]):
                    sub(s, i + 1, path + [s[j: i + 1]], out)

        sub(s, 0, [], out)
        return out