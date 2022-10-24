class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniq = ['']
        out = 0
        for i in range(len(arr)):
            for j in range(len(uniq)):
                temp = arr[i]+uniq[j]
                if len(temp)==len(set(temp)):
                    uniq.append(temp)
                    out=max(out,len(temp))

        return out