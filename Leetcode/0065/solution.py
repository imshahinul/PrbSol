class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r"^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
        return pattern.match(s.strip(" "))