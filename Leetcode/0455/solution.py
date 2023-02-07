class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        no_of_children = 0
        no_of_cookie = 0

        while no_of_children < len(g) and no_of_cookie < len(s):
            if s[no_of_cookie] >= g[no_of_children]:
                no_of_children += 1
            no_of_cookie += 1
        return no_of_children