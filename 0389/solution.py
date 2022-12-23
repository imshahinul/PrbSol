class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_t = {}
        for x in s:
            if x not in dict_t:
                dict_t[x] = 1
            else:
                dict_t[x] +=1
        for y in t:
            if y not in dict_t:
                return y
            else:
                dict_t[y] -=1
            if dict_t[y] == -1:
                return y