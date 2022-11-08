class Solution:
    def makeGood(self, s: str) -> str:
        flag = True
        good_s = []  # as stack
        for ch in s:
            if len(good_s) != 0 and (ord(good_s[-1]) == ord(ch) - 32 or ord(good_s[-1]) - 32 == ord(ch)):
                good_s.pop()
                flag = False
            if flag == True:
                good_s.append(ch)
            flag = True
        return "".join(good_s)