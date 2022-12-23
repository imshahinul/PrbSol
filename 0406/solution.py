class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        l = len(people)
        out = [[]] * l
        while people:
            ht,ppf = people.pop(0)
            c = ppf
            for k in range(l):
                if c == 0 and out[k] == []:
                    out[k] = [ht,ppf]
                    break
                elif not out[k] or (out[k][0] >= ht and out[k]):
                    c -= 1
        return out